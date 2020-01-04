from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import Worker


class ReloadPageConsumer(WebsocketConsumer):
    '''
    Класс который отвечает за отслеживание моделей и обновление страницы пользователя 
    который просматривает эту модель. 

    Чтоб добавить модель в отслеживание нужно:
    1) app.views добавить в context ключ 'room_name' с уникальным значением
       (если не уникальное, то будет производиться поиск по результату работы
       функции ReloadPageConsumer.get_data)
    2) Добавить в app.apps.appConfig.ready отслеживание

    3) Добавить в ReloadPageConsumer.get_data ключ (уникальное значение которое из view)
        и добавить ему list с названием этой модели. 

    '''

    def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['room_name']

        async_to_sync(self.channel_layer.group_add)(self.group_id, self.channel_name)
        async_to_sync(self.channel_layer.group_add)('all', self.channel_name)
        
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_id, self.channel_name)

    def filter(self, event):
        class_name = event['message']
        data = self.get_data()
        channel_layer = get_channel_layer()

        [
         async_to_sync(channel_layer.group_send)(id, {'type': 'reload_page'})
         for id in data
         if class_name in data[id]
        ]

    def reload_page(self, event):
        self.send(text_data=json.dumps({
            'reload_page': True
        }))

    def get_data(self):
        return {'1': ['Companies'], '2': ['Companies', 'Work', 'Worker', 'WorkPlace', 'Manager']}

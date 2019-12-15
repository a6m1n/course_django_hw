'''
Написать три celery таска (2 из них запустить их в разных очередях):
1) Таск который будет считывать информацию с апишки и заполнять информацию о рабочих в вашем проекте: https://jsonplaceholder.typicode.com/users
2) Таск который будет запускаться по расписанию, например раз в неделю, будет проверять сколько времени человек отработал на конкретном проекте за неделю. 
Лимит выставляет менеджер проекта (подумайте куда лучше всего добавить это поле) . 
Собирать данные об отработанном времени в отдельную таблицу Статистики.
Отправлять емейл менеджеру проекта если человек уже отработал больше лимитированого времени (в отдельном таске и в отдельной очереди)
'''

from __future__ import absolute_import, unicode_literals
from workers_management.celery import app
from works.models import Worker, Statistics, 

import requests
import datetime
import pytz



@app.task(name="works.tasks.read_api")
def read_api():

    def create_workers_from_json(json):
        for user in users:
            user = user['name'].split()
            Worker.object.create(
                first_name=user[0],
                last_name=user[1]
            )



    url = 'https://jsonplaceholder.typicode.com/users'
    r = requsts.get(url)
    return create_workers_from_json(r.json())


@app.task(name="works.tasks.one_user_limit_time_in_project")
def one_user_limit_time_in_project(user_id):

    user = Worker.objects.filter(id=user_id)
    
    curdate = datetime.datetime.now()-datetime.timedelta(days=7)
    curdate = pytz.UTC.localize(curdate)

    times = user.workplace.worktime_set.filter(date_start__gte=curdate)

    res = timedelta(hours=0)
    for time in times:
        res+=time.date_end-time.date_start

    limit = datetime.timedelta(hours=user.workplace.limit_hours)

    if limit<res:       
        print('send_message')
        # send_message()

    # Statistics.objects.create(
    #     worker=user,
    #     number_weak = len(user.statistics_set.all())+1 ,
    #     work_time_in_weak = res, 
    # )




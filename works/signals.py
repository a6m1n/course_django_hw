from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def signal_to_chanells(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    name_class = str(instance.__class__.__name__)
    async_to_sync(channel_layer.group_send)('all', {'type': 'filter', 'message': name_class})


import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Route
from .utils import serialize_state


class BusConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'bus_info'
        self.user = self.scope['user']
        if not self.user.is_authenticated:
            self.close()
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        if not (self.user.is_authenticated or not self.user.bus.is_admin):
            return

        try:
            json_data = json.loads(text_data)
            action = json_data['action']
            space = json_data['space_id']
            route_id = json_data['route_id']
            route = Route.objects.get(pk=route_id)

            if action == 'delay':
                route.status = 'd'
            if action == 'arrive':
                route.space = space
                route.status = 'a'
            if action == 'unarrive':
                route.space = None
                route.status = 'o'
            route.save()
        except:
            # TODO: catch exceptions
            pass

        message = serialize_state(None, user=self.user)

        self.send(text_data=json.dumps(message))

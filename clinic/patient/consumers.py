from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from django.shortcuts import render
from .models import QueueExamination, Examination
from django.utils.text import slugify
import re

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % slugify(self.room_name)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        room_name = re.sub(r'[^a-zA-Z0-9\-_]', '', self.room_name)
        self.room_group_name = 'chat_%s' % room_name

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        examinationId = data['examinationId']
        username = data['username']
        room = slugify(data['room'])
        await self.channel_layer.group_send(
            self.room_group_name, {
                'type': 'chat_message',
                'examinationId': examinationId,
                'username': username,
                'room': room,
            }
        )
        await self.save_examination(examinationId)

    async def chat_message(self, event):
        examinationId = event['examinationId']
        username = event['username']
        room = event['room']

        await self.send(text_data=json.dumps({
            'examinationId': examinationId,
            'username': username,
            'room': room,
        }))

    @sync_to_async
    def save_examination(self, examinationId):
        examination = Examination.objects.get(examination_id=examinationId)
        queue_examination = QueueExamination.objects.get(examination_id=examination)
        queue_examination.activate = True
        queue_examination.save()

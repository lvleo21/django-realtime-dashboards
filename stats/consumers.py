import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DashboardConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print("Connection...")
        await self.accept()
    
    async def disconnect(self, close_code):
        print(f"Connection close with code: {close_code}")
        
    
    async def receive(self, text_data):
        data = json.loads(text_data)

        message = data.get('message', None)
        sender = data.get('sender', None)


        print("Client: ", data)

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))



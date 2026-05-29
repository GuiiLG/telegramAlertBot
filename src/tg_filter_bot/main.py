from telethon import TelegramClient, events, sync
from dotenv import load_dotenv
import os


def main():
    load_dotenv()  # loads variables from .env into environment

    api_id = os.getenv("api_id")
    api_hash = os.getenv("api_hash")
    
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()

    mychannel = client.get_entity("https://t.me/+tZ_MCG46tWQyYjZh") 
    crownchannel = client.get_entity("https://t.me/crowmantech")

    keywords = ["ryzen 5 5500", "b450", "a520m", "b550", "kindle", "teclado", "rx", "rtx", "cadeira"]


    @client.on(events.NewMessage(chats=crownchannel))
    async def handler(event):
        for word in keywords:
            if word in event.message.text.lower():
                await client.send_message("me", event.message.text)

    print("Listening for new messages...")
    client.run_until_disconnected()



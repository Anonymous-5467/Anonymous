import os
import telethon
import asyncio
from datetime import datetime, timezone, timedelta
from telethon.errors import common
from telethon.sync import TelegramClient

api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
phone_number = os.getenv('TELEGRAM_PHONE_NUMBER')

client = telethon.sync.TelegramClient('session_name', api_id, api_hash)

async def update_name():
    await client.start(phone_number)

    # Set the timezone to IST
    ist = timezone(timedelta(hours=5, minutes=30))

    while True:
        try:
            # Get current time in IST using server time
            server_time = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(ist)
            current_time = server_time.strftime("%I:%M %p")
            new_name = f"{current_time} ＪＩＮＸＸ"
            new_username = "Jinxx6_6_fake2"
            await client(telethon.tl.functions.account.UpdateProfileRequest(first_name=new_name, about=new_name))
            print(f"Server time: {server_time}, Name updated to: {new_name}")
        except common.TypeNotFoundError as e:
            print(f"Ignoring TypeNotFoundError: {e}")

        # Update every minute (adjust as needed)
        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(update_name())

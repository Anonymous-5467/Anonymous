import os
import telethon
import asyncio
from telethon.errors import common
from telethon.sync import TelegramClient
import string
import random


bshwusbzws = "ANONYMOUS"
i28xvbaaj = list(bshwusbzws)
shuffle_count = 0

def get_name_bwwu():
  random.shuffle(i28xvbaaj)
  global shuffle_count
  shuffle_count += 1
  if shuffle_count == 5:
    shuffle_count = 0
    b2is8wbs = bshwusbzws
    return b2is8wbs
  else:
   b2is8wbs = "".join(i28xvbaaj)
   return b2is8wbs

api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
phone_number = os.getenv('TELEGRAM_PHONE_NUMBER')

client = telethon.sync.TelegramClient('session_name', api_id, api_hash)

async def update_name():
    await client.start(phone_number)

    while True:
        try:
            new_name = get_name_bwwu()
            await client(telethon.tl.functions.account.UpdateProfileRequest(first_name=new_name, about=new_name))
            print(f"Server time: {server_time}, Name updated to: {new_name}")
        except common.TypeNotFoundError as e:
            print(f"Ignoring TypeNotFoundError: {e}")

        await asyncio.sleep(60)
with client:
    client.loop.run_until_complete(update_name())
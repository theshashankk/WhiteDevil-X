# COPYRIGHT (C) 2021 BY LEGENDX22
"""
"""
# MADE BY LEGENDX22 🔥
# MY IDEA H YRR DONT KANG THIS PLEASE
import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
try:
  import LEGENDX
except:
  os.system("pip install LEGENDX")
try:
  from ULTRA import bot 
except:
  pass
from LEGENDX import devs, id, ID
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
import time
botnickname = os.environ.get("BOT_NICK_NAME")
ALIVE_NAME = os.environ.get("ALIVE_NAME")
BOT = str(botnickname) if botnickname else "Wʜɪᴛᴇ Dᴇᴠɪʟ X"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "Wʜɪᴛᴇ Dᴇᴠɪʟ X"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
ULTRAX = "[Wʜɪᴛᴇ Dᴇᴠɪʟ X](https://t.me/WHITEDEVILOT)"
VERSION = "0.0.1"
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_BOT_USERNAME = os.environ.get("ALIVE_BOT_USERNAME", None)
devs = devs
ID = ID
id = id
REPO = "[Wʜɪᴛᴇ Dᴇᴠɪʟ X](https://github.com/theshashankk/WhiteDevil-X)"

MASTER = NAME
GROUP = "[Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ](https://t.me/WhiteDevil_Support)"
if __name__=="__main__":
  bot.run()
  bot.run_until_disconnected()
  xbot.run_until_disconnected()

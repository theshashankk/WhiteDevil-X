#Copyright 2021-2022 Ultra X Bot
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ULTRA import ALIVE_NAME, StartTime
from ULTRA.utils import admin_cmd
from ULTRA import bot
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from ULTRA.helpers.functions import get_readable_time
import time
import os
import datetime
#importing finished
from ULTRA import botnickname 
BOT = str(botnickname) if botnickname else "Wʜɪᴛᴇ Dᴇᴠɪʟ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "Wʜɪᴛᴇ Dᴇᴠɪʟ"
tim = get_readable_time((time.time() - StartTime))
#pic 👇
PIC = os.environ.get("ALIVE_PIC")
#op 
uptime = tim
#time = date + time okay
TIME = time.asctime(time.localtime())
#my name 👇
ULTRAX = "[Wʜɪᴛᴇ Dᴇᴠɪʟ X](https://t.me/whitedevilot)"
#my bots repo 👇
REPO = "[Wʜɪᴛᴇ Dᴇᴠɪʟ X](https://github.com/theshashankk/WhiteDevil-X)"
#grpup👇NAME = "[{MAATER}](tg://user?id={X})"
#yrr isko apne bot me aply krne se pehle mere se pooch lena ok
#aur aage add kruga abhi busy okay 🤔
global ghanti
X = bot.uid
MASTER = f"[{NAME}](tg://user?id={X})"
GROUP = "[SUPPORT GROUP](https://t.me/ULTRAXCHAT)"
#itna test h aur aage krte h
#test successful raha ab aage 
ALIVE = "աɦɨȶɛ ɖɛʋɨʟ Ӽ ɨֆ օռ 🔥 ʄɨʀɛ 🔥" 
OP = " ɦɛʟʟօ ʍǟֆȶɛʀ ʍʏ ռǟʍɛ ɨֆ աɦɨȶɛ ɖɛʋɨʟ χ ɮօȶ ǟռɖ ɨ ʍ ȶɦɛ ɮɛֆȶ ʊֆɛʀɮօȶ 💝"
EMOJI = "🔥"

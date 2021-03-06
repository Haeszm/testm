import asyncio

from pyrogram import Client, filters

from strings import get_command

from strings.filters import command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP

from YukkiMusic import app

from config import BANNED_USERS, MUSIC_BOT_NAME

from YukkiMusic.misc import SUDOERS

import re

import sys

from os import getenv

from dotenv import load_dotenv

from pyrogram import filters

import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from YukkiMusic.misc import SUDOERS

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

OWNER = getenv("OWNER")

ID_BOT1 = getenv("ID_BOT1")

NAME_BOT = getenv("NAME_BOT")

DEV = getenv("DEV")

def get_file_id(msg: Message):

    if msg.media:

        for message_type in (

            "photo",

            "animation",

            "audio",

            "document",

            "video",

            "video_note",

            "voice",

            # "contact",

            # "dice",

            # "poll",

            # "location",

            # "venue",

            "sticker",

        ):

            obj = getattr(msg, message_type)

            if obj:

                setattr(obj, "message_type", message_type)

                return obj


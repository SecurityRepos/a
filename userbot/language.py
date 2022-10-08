# © Copyright Brend Userbot 
# t.me/BrendOwner tərəfindən xəta düzəldilmişdir
# Baxıb öyrənərsən))

from . import LANGUAGE, LOGS, bot
from json import loads, JSONDecodeError
from os import path, remove
from telethon.tl.types import InputMessagesFilterDocument

LANGUAGE_JSON = None

if LANGUAGE_JSON == None:
    if path.isfile(f"./userbot/language/{LANGUAGE}.brendjson"):
        try:
            LANGUAGE_JSON = loads(open(f"./userbot/language/{LANGUAGE}.brendjson", "r").read())
        except JSONDecodeError:
            raise Exception("Invalid json file")
    else:
        if path.isfile("./userbot/language/DEFAULT.brendjson"):
            LOGS.warn("Default dil faylı istifadə olunur...")
            LANGUAGE_JSON = loads(open(f"./userbot/language/DEFAULT.brendjson", "r").read())
        else:
            raise Exception(f"Didn't find {LANGUAGE} file")

def get_value (plugin = None, value = None):
    global LANGUAGE_JSON

    if LANGUAGE_JSON == None:
        raise Exception("Please load language file first")
    else:
        if not plugin == None or value == None:
            Plugin = LANGUAGE_JSON.get("STRINGS").get(plugin)
            if Plugin == None:
                raise Exception("Invalid plugin")
            else:
                String = LANGUAGE_JSON.get("STRINGS").get(plugin).get(value)
                if String == None:
                    return Plugin
                else:
                    return String
        else:
            raise Exception("Invalid plugin or string")

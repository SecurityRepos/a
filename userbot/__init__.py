import os
from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb
from requests import get
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
    
BREND_VERSION = "v5"
API_ID = int(os.environ.get("API_KEY", "1558926"))
API_HASH = os.environ.get("API_HASH", "69c4c16e17e9f637818f2cfce8f9bce5")
STRING_SESSION = os.environ.get("STRING_SESSION", None)

# LOG Group
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID") or 0)
BOTLOG = sb(os.environ.get("BOTLOG", "False"))
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER", "False"))
CONSOLE_LOGGER_VERBOSE = sb(os.environ.get("CONSOLE_LOGGER_VERBOSE", "False"))
PM_AUTO_BAN = sb(os.environ.get("PM_AUTO_BAN", "False"))
PM_AUTO_BAN_LIMIT = int(os.environ.get("PM_AUTO_BAN_LIMIT", 4))

# Heroku
HEROKU_APPNAME = os.environ.get("HEROKU_APPNAME", None)
HEROKU_APIKEY = os.environ.get("HEROKU_APIKEY", None)
DB_URI = os.environ.get("DATABASE_URL", "sqlite:///brend.db")

CMD_HELP = []
WARN_LIMIT = int(os.environ.get("WARN_LIMIT", 3))
WARN_MODE = os.environ.get("WARN_MODE", "gmute")
if not WARN_MODE in ["gmute", "gban"]:
    WARN_MODE = "gmute"

PLUGIN_ID = os.environ.get("PLUGIN_ID", "me")
CLEAN_WELCOME = sb(os.environ.get("CLEAN_WELCOME", "True"))
PATTERNS = os.environ.get("PATTERNS", ".")
LANGUAGE = os.environ.get("LANGUAGE", "AZ").upper()
if not LANGUAGE == "AZ":
    LOGS.info("Naməlum bir dil yazdınız. Buna görə AZ dili istifadə olunur.")
    LANGUAGE = "AZ"

BRAIN_CHECKER = []
WHITELIST = get('https://gitlab.com/brenduserbot/brend-userbot/-/raw/master/whitelist.json').json()
SUPPORT = get('https://gitlab.com/brenduserbot/brend-userbot/-/raw/master/support.json').json()
HUSU = get('https://gitlab.com/brenduserbot/brend-userbot/-/raw/master/husu.json').json()
SUP = [-1001197418406]

if CONSOLE_LOGGER_VERBOSE:
    basicConfig(format="@BrendUserBot - %(levelname)s - %(message)s", level=DEBUG)
else:
    basicConfig(format="@BrendUserBot - %(levelname)s - %(message)s", level=INFO)
LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 8:
    LOGS.info("Botun işləməsi üçün ən az python 3.8 versiyanız olmalıdır.")
    quit(1)

if STRING_SESSION:
    bot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
else:
    bot = TelegramClient("brend", API_ID, API_HASH)

if os.path.exists("brend.check"):
    os.remove("brend.check")

with open('brend.check', 'wb') as load:
    load.write(get('https://gitlab.com/brenduserbot/brend-userbot/-/raw/master/brend.check').content)

async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        await bot.send_message(me, "LogSpammer özəlliyinin aktivləşməsi üçün BOTLOG_CHATID qrupunuz olmalıdır.")
        quit(1)
    elif not BOTLOG_CHATID and BOTLOG:
        await bot.send_message(me, "BOTLOG özəlliyini aktiv etmək üçün BOTLOG_CHATID dəyərini doldurun.")
        quit(1)
    elif not BOTLOG or not LOGSPAMMER:
        return
    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        await bot.send_message(me, "Hesabınızla BOTLOG qrupuna mesaj göndərmək olmur./nQrup ID-sini düzgünlüyündən əmin olun.")
        quit(1)


with bot:
    try:
        bot(JoinChannelRequest("@BrendUserbot"))
        bot(JoinChannelRequest("@BrendSupport"))
    except:
        pass
    try:
        bot.loop.run_until_complete(check_botlog_chatid())
    except:
        await bot.send_message(me, "BOTLOG_CHATID yeniləməyiniz tövsiyyə olunur.")
        quit(1)

    me = bot.get_me()
    uid = me.id
    ALIVE_NAME = f"{me.first_name}"
    DEFAULT_NAME = f"{me.first_name}"
    BREND_MENTION = f"[{DEFAULT_NAME}](tg://user?id={SAHIB})"

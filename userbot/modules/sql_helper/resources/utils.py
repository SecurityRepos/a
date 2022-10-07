import heroku3
from telethon.tl.functions.channels import CreateChannelRequest
from userbot import HEROKU_APIKEY, HEROKU_APPNAME, bot

if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None:
    Heroku = heroku3.from_key(HEROKU_APIKEY)
    app = Heroku.app(HEROKU_APPNAME)
    heroku_var = app.config()
else:
    app = None

async def autobotlog():
    try:
        qrup = await bot(CreateChannelRequest(title="⚡ Brend Botlog", about="⚡ Brend Userbot Botlog.", megagroup=True))
        qrup_id = qrup.chats[0].id
    except Exception as e:
        LOGS.error(str(e))
    if not str(qrup_id).startswith("-100"):
        qrup_id = int(f"-100{str(qrup_id)}")
    heroku_var["BOTLOG"] = "True"
    heroku_var["BOTLOG_CHATID"] = qrup_id

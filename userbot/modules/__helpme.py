# Copyright Brend Userbot
# Bu modul Brend Userbota Məxsusdur

from userbot import BOT_USERNAME
from userbot.events import register
from userbot.language import get_value
LANG = get_value("__helpme")

@register(outgoing=True, pattern="^.help$")
async def help(event):
    brend = BOT_USERNAME
    results = await event.client.inline_query(brend, "@BrendUserbot")
    await results[0].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
    await event.delete()

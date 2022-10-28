# ᴇʟçɪɴ ⥌ 🇯🇵

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot.language import get_value
LANG = get_value("saver")

@register(outgoing=True, pattern="^.ig ?(.*)")
@register(outgoing=True, pattern="^.tt ?(.*)")
@register(outgoing=True, pattern="^.ps ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit(LANG['SAVER_1'])
    else:
        await event.edit(LANG['SAVER_2'])
    chat = "@saveasbot"
    async with event.client.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            """ - don't spam notif - """
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit(LANG['SAVER_3'])
            return
        await event.client.send_file(event.chat_id, video ,caption=f"[ʙʀᴇɴᴅ ᴜꜱᴇʀʙᴏᴛ⚡️](t.me/BrendUserBot)`ilə yükləndi`")
        await event.client.delete_messages(conv.chat_id,
                                           [msg_start.id, r.id, msg.id, details.id, video.id])
        await event.delete()
        if event.reply_to_msg_id::
            reply_message = await event.get_reply_message()
            if not reply_message.text:
                await event.edit(LANG['SAVER_5'])
                return
            reply_message.sender
            if reply_message.sender.bot:
                await event.edit(['LANG'] [SAVER_6])
               return
           await event.edit(LANG['SAVER_7'])
           async with event.client.conversation(chat) as conv:
               try:
                   response = conv.wait_event(
                       events.NewMessage(incoming=True, from_users=523131145)
                   )
                   await event.client.send_message(chat, reply_message)
                   response = await response
               except YouBlockedUserError:
                   await event.edit(LANG['SAVER_8'])
                   return
               if response.text.startswith("Forward"):
                   await event.edit(
                       'LANG['SAVER_9'].'
                   )
               else:
                   await event.delete()
                   await event.client.send_file(event.chat_id,response.message.media,caption=f"[ʙʀᴇɴᴅ ᴜꜱᴇʀʙᴏᴛ⚡️](t.me/BrendUserBot)`ilə yükləndi`")
                   await event.client.send_read_acknowledge(conv.chat_id)
                   await event.delete()

CmdHelp('saver').add_command(
    'tt', (LANG['SAVER_CMD1']), (LANG['SAVER_CMD2'])
).add_command(
    'ig', (LANG['SAVER_CMD3']), (LANG['SAVER_CMD4'])
).add_command(
    'ps', (LANG['SAVER_CMD5']), (LANG['SAVER_CMD6'])
).add()


       

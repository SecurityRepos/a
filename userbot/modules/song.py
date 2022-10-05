import asyncio, os, json, base64
from requests import get
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP, DEFAULT_NAME
from userbot.events import register
from random import randint
from userbot.cmdhelp import CmdHelp
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import ExtractorError
from youtube_search import YoutubeSearch
from userbot.language import get_value
LANG = get_value("song")

@register(outgoing=True, pattern="^.deez(\d*|)(?: |$)(.*)")
async def deezl(event):
    if event.fwd_from:
        return
    sira = event.pattern_match.group(1)
    if sira == '':
        sira = 0
    else:
        sira = int(sira)
    mahni = event.pattern_match.group(2)
    if len(mahni) < 1:
        if event.is_reply:
            sarki = await event.get_reply_message().text
        else:
            await event.edit(LANG['GIVE_ME_SONG']) 
    await event.edit(LANG['SEARCHING'])
    chat = "@DeezerMusicBot"
    async with bot.conversation(chat) as conv:
        try:     
            mesaj = await conv.send_message(str(randint(31,62)))
            mahnilar = await conv.get_response()
            await mesaj.edit(mahni)
            mahnilar = await conv.get_response()
        except YouBlockedUserError:
            await event.reply(LANG['BLOCKED_DEEZER'])
            return
        await event.client.send_read_acknowledge(conv.chat_id)
        if mahnilar.audio:
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, LANG['UPLOADED_WITH'], file=mahnilar.message)
            await event.delete()
        elif mahnilar.buttons[0][0].text == "No results":
            await event.edit(LANG['NOT_FOUND'])
        else:
            await mahnilar.click(sira)
            mahni = await conv.wait_event(events.NewMessage(incoming=True,from_users=595898211))
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, f"`{mahnilar.buttons[sira][0].text}` | " + LANG['UPLOADED_WITH'], file=mahni.message)
            await event.delete()

@register(outgoing=True, pattern=r"^.song (.*)")
async def mahniyukle(event):
    a = event.text
    await event.edit("🔎Musiqi axtarılır, xahiş edirəm bir az gözləyin...")
    url = event.pattern_match.group(1)
    if not url:
        return await event.edit("**❌ Axtarış Xətası**\n\n✍🏻 İstifadə qaydası: -`.song Aşıl Empati`")
    results = []
    results = YoutubeSearch(url, max_results=1).to_dict()
    try:
        url = f"https://youtube.com{results[0]['url_suffix']}"
    except BaseException:
        return await event.edit("🤦🏻‍♂️ Mahnını tapa bilmirəm...")
    await event.edit(f"📥 Hazırdır Endirilir...")
    opts = {
        "outtmpl": "%(title)s.m4a",
        "writethumbnail": True,
        "format": "bestaudio/best",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
    }
    try:
        await event.edit("🔄 Musiqi məlumatı əldə olunur...")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except Exception as e:
        return await event.edit(f"{e}")
    thumb = "userbot/modules/sql_helper/resources/Brend_Logo.jpg"
    await event.edit(f"📥 Yüklənir...\n• 🎶 Mahnı: {rip_data['title']}\n• 📡 Kanal: {rip_data['uploader']}")
    CAPT = f"╰┈───────────────┈╮\n➥ 🎵 {rip_data['title']}\n➥ 📡 Kanal: {rip_data['uploader']}\n╭┈───────────────┈╯\n➥ 👤 Sahibim: {DEFAULT_NAME}\n╰┈───────────────┈➤"
    await event.delete()
    await event.client.send_file(
        event.chat_id,
        f"{rip_data['id']}.m4a",
        thumb=thumb,
        supports_streaming=True,
        caption=CAPT,
        attributes=[
            DocumentAttributeAudio(
                duration=int(rip_data["duration"]),
                title=str(rip_data["title"]),
                performer=str(rip_data["uploader"]),
            )
        ],
    )
    os.remove(f"{rip_data['id']}.m4a")

@register(outgoing=True, pattern=r"^.lyrics (.*)")
async def lyrics(event):
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("**Zəhmət olmasa mahnının adını daxil edin**")
    try:
        await event.edit("`Mahnı sözləri axtarılır...`")
        respond = requests.get(f"https://api-tede.herokuapp.com/api/lirik?l={query}").json()
        result = f"{respond['data']}"
        await event.edit(result)
    except Exception:
        await event.edit("**Mahnının sözləri tapılmadı.**")


CmdHelp('song').add_command(
    'deez', '<mahnı adı>', 'Deezerdən mahnı atar.'
).add_command(
    'song', '<mahnı adı>', 'Mahnı yükləyər.'
).add_command(
    'lyrics', '<mahnı adı>', 'Mahnının sözlərini axtarar'
).add()

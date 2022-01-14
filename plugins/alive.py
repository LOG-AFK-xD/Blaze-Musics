import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ceea3d2fbda7b1a0c9f17.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
❣️        𝗕ʟᴀᴢᴇ 𝗠ᴜ𝘀ɪᴄ 𝗥ᴏʙᴏᴛ               ❣️
┏━━━━━━━━━━━━━━━━━┓
┣★ 𝐂ʀᴇᴀᴛᴏʀ : [𝐎ғғɪᴄɪᴀʟ 𝐀ғᴋ𝐱𝐃](https://t.me/log_afk)
┣★ 𝐒ᴜᴘᴘᴏʀᴛ : [𝐁ʟᴀᴢᴇ 𝐒ᴜᴘᴘᴏʀᴛ](https://t.me/Blaze_support)
┣★ 𝐂ʜᴀᴛ𝐙ᴏɴ : [𝐂ʜᴀᴛᴛɪɴɢ 𝐆ʀᴏᴜ.](https://t.me/UNIQUE_SOCIETY)
┣★ 𝐅ʀɪᴇɴᴅ𝐬  : [𝐈ɴɴᴏᴄᴇɴᴛ 𝐏ᴇʀ𝐬.](https://t.me/evil_xD_boy)
┗━━━━━━━━━━━━━━━━━┛
💞 𝐈ғ ᴜ ʜᴀᴠᴇ ᴀɴʏ ϙᴜᴇ𝐬ᴛɪᴏɴ𝐬 
 𝐃ᴍ ᴛᴏ 𝐌ʏ[𝗖ᴀᴘᴛᴀɪɴ 𝗔ɴᴅʏ](https://t.me/its_jack) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝐀ᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ 𝐆ʀᴏᴜᴘ ➕", url="t.me/BLAZE_MUSIC_BOT?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "sᴀʟɪᴍ"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ceea3d2fbda7b1a0c9f17.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥𝐉ᴏɪɴ 𝐀ɴᴅ 𝐒ᴛᴀʏ 𝐔ᴘᴅᴀᴛᴇᴅ 🥀 ", url=f"https://t.me/The_Blaze_Fighter")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ceea3d2fbda7b1a0c9f17.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❣️ 𝗖ʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ 𝗥ᴇᴘᴏ 💞", url=f"HTTPS://T.ME/HARSH_pandit_xD")
                ]
            ]
        ),
    )

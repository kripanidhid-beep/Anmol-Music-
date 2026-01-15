import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from yt_dlp import YoutubeDL
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME

# Setup
bot = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
assistant = Client("Assistant", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_NAME)
call_py = PyTgCalls(assistant)

@bot.on_message(filters.command("play") & filters.group)
async def play_music(_, message):
    if len(message.command) < 2:
        return await message.reply("🔎 Gaane ka naam likho!")
    query = " ".join(message.command[1:])
    m = await message.reply("🔄 Searching...")
    try:
        with YoutubeDL({"format": "bestaudio", "quiet": True}) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"][0]
            url = info["url"]
            title = info["title"]
        await call_py.play(message.chat.id, AudioPiped(url))
        await m.edit(f"▶️ **Playing:** {title}")
    except Exception as e:
        await m.edit(f"❌ Error: {e}")

async def start():
    await bot.start()
    await call_py.start()
    print("🚀 BOT IS LIVE!")
    await asyncio.Idle()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start())
    

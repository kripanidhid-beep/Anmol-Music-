import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from yt_dlp import YoutubeDL
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME

# Clients Setup
bot = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
assistant = Client("Assistant", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_NAME)
call_py = PyTgCalls(assistant)

def get_audio_url(query):
    ydl_opts = {"format": "bestaudio/best", "quiet": True}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"][0]
        return info["url"], info["title"]

@bot.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply_text("🔎 Gaane ka naam likho!")
    
    m = await message.reply_text("🔄 **Searching...**")
    try:
        audio_url, title = get_audio_url(query)
        await call_py.join_group_call(message.chat.id, AudioPiped(audio_url))
        await m.edit(f"▶️ **Playing:** `{title}`")
    except Exception as e:
        await m.edit(f"❌ **Error:** {e}")

@bot.on_message(filters.command("stop") & filters.group)
async def stop_music(client, message):
    try:
        await call_py.leave_group_call(message.chat.id)
        await message.reply_text("⏹️ **Stopped.**")
    except:
        await message.reply_text("❌ Nothing is playing.")

async def start_bot():
    print("✅ Bot start ho raha hai...")
    await bot.start()
    await call_py.start()
    print("🚀 Bot Online!")
    await asyncio.Idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    

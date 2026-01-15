import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped
from yt_dlp import YoutubeDL
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME

# 1. Bot aur Assistant setup
bot = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
assistant = Client("Assistant", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_NAME)
call_py = PyTgCalls(assistant)

# 2. YouTube Search Function
def get_audio_url(query):
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch:{query}", download=False)
        info = search_results["entries"][0]
        return info["url"], info["title"]

# 3. /play Command
@bot.on_message(filters.command("play") & filters.group)
async def play_music(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Gaane ka naam likho! \nExample: `/play tum hi ho`")

    query = " ".join(message.command[1:])
    m = await message.reply_text("🔎 **Searching...**")

    try:
        audio_url, title = get_audio_url(query)
        await call_py.join_group_call(
            message.chat.id,
            AudioPiped(audio_url),
            stream_type=StreamType().pulse_stream,
        )
        await m.edit(f"▶️ **Playing:** `{title}`\n\n💡 Group ki Voice Chat on honi chahiye!")
    except Exception as e:
        await m.edit(f"❌ **Error:** {e}")

# 4. /stop Command
@bot.on_message(filters.command("stop") & filters.group)
async def stop_music(client, message):
    try:
        await call_py.leave_group_call(message.chat.id)
        await message.reply_text("⏹️ **Music Stopped.**")
    except:
        await message.reply_text("❌ Abhi koi gaana nahi chal raha.")

# 5. Bot Start karna
async def start_bot():
    print("✅ Bot aur Assistant start ho rahe hain...")
    await bot.start()
    await call_py.start()
    print("🚀 Bot Online hai!")
    await asyncio.Idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
    

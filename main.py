from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

# Bot Client Setup
bot = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text(f"Namaste {message.from_user.mention}!\nMain ek Music Bot hoon. Mujhe group mein add karo gaane sunne ke liye.")

print("Bot shuru ho raha hai...")
bot.run()


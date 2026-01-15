import os

# Telegram API Details
API_ID = int(os.getenv("API_ID", "123456")) # Yahan default ki jagah apni ID bhi daal sakte ho
API_HASH = os.getenv("API_HASH", "abcd1234")

# Bot Token aur Session String
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME") # Aapki Pyrogram Session String

# MongoDB URI (Data save karne ke liye)
MONGO_DB_URI = os.getenv("MONGO_DB_URI")

# Owner ID (Aapki Telegram ID)
OWNER_ID = int(os.getenv("OWNER_ID", "00000000"))


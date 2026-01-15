
import os

API_ID = int(os.getenv("API_ID", "12345")) # Apna API ID daalein
API_HASH = os.getenv("API_HASH", "abcd")   # Apna API Hash daalein
BOT_TOKEN = os.getenv("BOT_TOKEN")         # @BotFather wala Token
SESSION_NAME = os.getenv("SESSION_NAME")   # Assistant ki Session String
OWNER_ID = int(os.getenv("OWNER_ID", "0")) # Aapki Telegram ID

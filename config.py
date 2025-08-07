import os
from dotenv import load_dotenv

load_dotenv()

# Website settings
TARGET_URL = os.getenv("TARGET_URL")
BUTTON_TEXT_TO_WATCH = os.getenv("BUTTON_TEXT_TO_WATCH")

# Discord settings
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

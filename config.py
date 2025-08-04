import os
from dotenv import load_dotenv

load_dotenv()

# Website settings
TARGET_URL = "https://teatrocolon.org.ar/produccion/estonian-philharmonic-chamber-choir/"
BUTTON_TEXT_TO_WATCH = "Próximamente"

# Check if we're in test mode
TEST_MODE = os.getenv("TEST_MODE", "false").lower() == "true"
CHECK_INTERVAL_HOURS = 1/60 if TEST_MODE else 1  # 1 minute in test mode, 1 hour normally

# Discord settings
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Logging
LOG_LEVEL = "INFO"
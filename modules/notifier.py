import requests
import logging
from config import DISCORD_WEBHOOK_URL

def send_discord_notification(message, title="Colón Alert"):
    """
    Send a notification to Discord via webhook
    """
    if not DISCORD_WEBHOOK_URL:
        logging.error("Discord webhook URL not configured")
        return False
    
    # Create embed for prettier message
    embed = {
        "title": title,
        "description": message,
        "color": 0x00ff00,  # Green color
        "timestamp": None
    }
    
    payload = {
        "embeds": [embed]
    }
    
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        logging.info("Discord notification sent successfully")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send Discord notification: {e}")
        return False

def send_status_update(status, url, button_text=None):
    """
    Send a status update about the check
    """
    if status == "tickets_available":
        message = f"🎉 **TICKETS ARE NOW AVAILABLE!** 🎉\n\nCheck the website: {url}"
        title = "🎫 Tickets Available!"
    elif status == "button_changed":
        message = f"⚠️ Button text changed!\n\nNew text: '{button_text}'\nURL: {url}"
        title = "🔄 Button Changed"
    elif status == "error":
        message = f"❌ Error checking website: {url}\n\nPlease check the logs."
        title = "⚠️ Error"
    elif status == "test":
        message = f"🧪 Test notification from Colón\n\nTarget URL: {url}\n\nIf you see this, notifications are working! ✅"
        title = "🧪 Test Notification"
    else:
        message = f"Status: {status}\nURL: {url}"
        title = "Colón Update"
    
    return send_discord_notification(message, title)
import logging
import schedule
import time
from modules.web_scraper import check_tickets
from modules.notifier import send_status_update
from config import TARGET_URL, TEST_MODE, LOG_LEVEL

def setup_logging():
    """
    Configure logging to both file and console
    """
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/main.log'),
            logging.StreamHandler()  # This prints to console too
        ]
    )

def run_check():
    """
    Run a single check
    """
    try:
        logging.info("Starting check...")
        status, message = check_tickets()
        
        if status == "no_change":
            logging.info(f"No change detected: {message}")
        elif status == "changed":
            logging.warning(f"CHANGE DETECTED: {message}")
            send_status_update("button_changed", TARGET_URL, message)
        elif status == "error":
            logging.error(f"Error during check: {message}")
            send_status_update("error", TARGET_URL)
            
    except Exception as e:
        logging.error(f"Unexpected error during check: {e}")
        send_status_update("error", TARGET_URL)

def main():
    """
    Main function to start colon
    """
    print("🎫 Colón Starting...")
    setup_logging()
    
    # Send startup notification
    send_status_update("started", TARGET_URL)
    logging.info("Colón started successfully")
    
    # Schedule the check to run at the top of every hour
    if TEST_MODE:
        # In test mode, run every minute at the top of the minute
        schedule.every().minute.at(":00").do(run_check)
        print(f"🕐 Scheduled to check every minute at :00 seconds (TEST MODE)")
    else:
        # Run every hour at the top of the hour
        schedule.every().hour.at(":00").do(run_check)
        print(f"🕐 Scheduled to check every hour at :00 minutes")
    
    # Run an initial check immediately
    run_check()
    
    print(f"✅ Monitoring {TARGET_URL}")
    print("📱 Notifications will be sent to Discord")
    print("🛑 Press Ctrl+C to stop")
    
    # Keep the script running
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute if it's time to run
    except KeyboardInterrupt:
        logging.info("Colón stopped by user")
        print("\n👋 Colón stopped!")

if __name__ == "__main__":
    main()
import logging
import schedule
import time
from modules.web_scraper import check_tickets
from modules.notifier import send_status_update
from config import TARGET_URL, CHECK_INTERVAL_HOURS, LOG_LEVEL

def setup_logging():
    """
    Configure logging to both file and console
    """
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/ticket_checker.log'),
            logging.StreamHandler()  # This prints to console too
        ]
    )

def run_check():
    """
    Run a single ticket check
    """
    try:
        logging.info("Starting ticket check...")
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
    Main function to start the ticket checker
    """
    print("🎫 Ticket Checker Starting...")
    setup_logging()
    
    # Send startup notification
    send_status_update("started", TARGET_URL)
    logging.info("Ticket checker started successfully")
    
    # Schedule the check to run every hour
    schedule.every(CHECK_INTERVAL_HOURS).hours.do(run_check)
    
    # Run an initial check immediately
    run_check()
    
    print(f"✅ Monitoring {TARGET_URL}")
    print(f"🕐 Checking every {CHECK_INTERVAL_HOURS} hour(s)")
    print("📱 Notifications will be sent to Discord")
    print("🛑 Press Ctrl+C to stop")
    
    # Keep the script running
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute if it's time to run
    except KeyboardInterrupt:
        logging.info("Ticket checker stopped by user")
        print("\n👋 Ticket checker stopped!")

if __name__ == "__main__":
    main()
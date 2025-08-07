import logging
from modules.web_scraper import check_tickets
from modules.notifier import send_status_update
from config import TARGET_URL

def setup_logging():
    """
    Configure logging to console
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
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
    Main function - performs a single check and exits
    """
    setup_logging()
    run_check()

if __name__ == "__main__":
    main()
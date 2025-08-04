import requests
from bs4 import BeautifulSoup
import logging
from config import TARGET_URL, BUTTON_TEXT_TO_WATCH

def fetch_webpage(url):
    """
    Fetch the webpage content
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching webpage: {e}")
        return None

def check_button_status(html_content):
    """
    Parse HTML and check if the button text has changed
    """
    if not html_content:
        return None, "Error fetching page"
    
    try:
        soup = BeautifulSoup(html_content, 'lxml')  # Explicitly specify lxml parser
        
        # Look for buttons or links that might contain our target text
        # We'll search in multiple places since we don't know the exact structure
        potential_elements = soup.find_all(['button', 'a', 'span', 'div'], 
                                         string=lambda text: text and BUTTON_TEXT_TO_WATCH.lower() in text.lower())
        
        if potential_elements:
            # Found the expected text
            return True, BUTTON_TEXT_TO_WATCH
        else:
            # Text not found - might have changed!
            # Let's look for common ticket-related terms
            ticket_keywords = ['comprar', 'entradas', 'tickets', 'disponible', 'agotado']
            for keyword in ticket_keywords:
                elements = soup.find_all(['button', 'a', 'span', 'div'], 
                                       string=lambda text: text and keyword.lower() in text.lower())
                if elements:
                    return False, elements[0].get_text().strip()
            
            return False, "Button text changed (couldn't find expected text)"
            
    except Exception as e:
        logging.error(f"Error parsing HTML: {e}")
        return None, f"Parse error: {e}"

def check_tickets():
    """
    Main function to check if tickets are available
    """
    logging.info(f"Checking {TARGET_URL}")
    
    html_content = fetch_webpage(TARGET_URL)
    if not html_content:
        return "error", "Failed to fetch webpage"
    
    has_expected_text, current_text = check_button_status(html_content)
    
    if has_expected_text is None:
        return "error", current_text
    elif has_expected_text:
        return "no_change", current_text
    else:
        return "changed", current_text
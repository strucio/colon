#!/usr/bin/env python
"""
Simple test script to verify the ticket checker works
"""
from modules.web_scraper import check_tickets
from modules.notifier import send_status_update
from config import TARGET_URL

def test_scraper():
    """Test the web scraper"""
    print("🧪 Testing web scraper...")
    status, message = check_tickets()
    print(f"Status: {status}")
    print(f"Message: {message}")
    return status != "error"

def test_discord():
    """Test Discord notification"""
    print("🧪 Testing Discord notification...")
    return send_status_update("started", TARGET_URL)

if __name__ == "__main__":
    print("🧪 Running tests...\n")
    
    scraper_ok = test_scraper()
    print(f"Web scraper: {'✅ OK' if scraper_ok else '❌ FAILED'}\n")
    
    discord_ok = test_discord()
    print(f"Discord notifications: {'✅ OK' if discord_ok else '❌ FAILED'}\n")
    
    if scraper_ok and discord_ok:
        print("🎉 All tests passed! Ready to run the main script.")
    else:
        print("❌ Some tests failed. Check your configuration.")
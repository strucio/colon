# 🎫 Colon

A Python-based monitoring tool that automatically checks for ticket availability and sends Discord notifications when changes are detected.

## 📋 Prerequisites

- Docker installed on your system
- Discord server with webhook configured

## 🛠️ Quick Setup

### Option 1: Using the setup script (Recommended)

```bash
# Clone or download the repository
git clone https://github.com/Strucio/colon
cd ticket-checker

# Run the setup script
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual setup

1. **Configure environment variables**:

   ```bash
   cp .example.env .env
   # Edit .env with your Discord webhook URL
   ```

2. **Build and run with Docker**:

   ```bash
   docker build -t ticket-checker .
   docker run -d --name ticket-checker --env-file .env ticket-checker
   ```

## ⚙️ Configuration

Edit the `.env` file with your settings:

```env
# Discord webhook URL (required)
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your-webhook-url

# Test mode - checks every minute instead of every hour
TEST_MODE=false
```

### Setting up Discord Webhook

1. Go to your Discord server settings
2. Navigate to Integrations → Webhooks
3. Click "New Webhook"
4. Choose a channel and copy the webhook URL
5. Paste it in your `.env` file

## 🎯 Target Configuration

To monitor a different website, edit `config.py`:

```python
TARGET_URL = "https://your-target-website.com"
BUTTON_TEXT_TO_WATCH = "Text to monitor for changes"
```

## 🐳 Docker Commands

```bash
# Build the image
docker build -t ticket-checker .

# Run the container
docker run -d --name ticket-checker --env-file .env ticket-checker

# View logs
docker logs ticket-checker

# Follow logs in real-time
docker logs -f ticket-checker

# Stop the container
docker stop ticket-checker

# Start the container
docker start ticket-checker

# Remove the container
docker rm ticket-checker
```

## 🧪 Testing

Run the test script to verify everything works:

```bash
python test_checker.py
```

Or test individual components:

```bash
# Test web scraping
python -c "from modules.web_scraper import check_tickets; print(check_tickets())"

# Test Discord notifications
python -c "from modules.notifier import send_status_update; send_status_update('started', 'test')"
```

## 📊 Monitoring

The application provides several ways to monitor its status:

- **Discord notifications** for important events
- **Log files** in the `logs/` directory
- **Console output** when running locally
- **Docker logs** when running in container

### Log Levels

- `INFO`: Normal operation messages
- `WARNING`: Important changes detected
- `ERROR`: Problems that need attention

## 🔧 Development

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally (for testing)
python ticket_checker.py
```

### Project Structure

```sh
├── config.py              # Configuration settings
├── ticket_checker.py      # Main application
├── test_checker.py        # Test script
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── setup.sh               # Setup script
├── modules/
│   ├── notifier.py        # Discord notification handler
│   └── web_scraper.py     # Web scraping logic
└── logs/                  # Log files directory
```

## 🚨 Troubleshooting

### Common Issues

**Docker container stops immediately**:

- Check if `.env` file exists and contains valid Discord webhook URL
- View logs: `docker logs ticket-checker`

**No notifications received**:

- Verify Discord webhook URL is correct
- Test with: `python test_checker.py`

**Website parsing errors**:

- Website structure may have changed
- Check logs for specific error messages
- May need to update parsing logic in `web_scraper.py`

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `DISCORD_WEBHOOK_URL` | Discord webhook URL for notifications | Yes | - |
| `TEST_MODE` | Enable test mode (1-minute intervals) | No | `false` |

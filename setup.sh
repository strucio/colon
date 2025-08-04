#!/bin/bash
echo "🎫 Installing Ticket Checker..."

# Pull the image
docker pull strucio/colon:latest

# Create .env file template
cat > .env << EOF
DISCORD_WEBHOOK_URL=your-webhook-url-here
TEST_MODE=false
EOF

echo "✅ Installation complete!"
echo "📝 Edit .env file with your Discord webhook URL"
echo "🚀 Run with: docker run -d --name ticket-checker --env-file .env strucio/colon:latest"
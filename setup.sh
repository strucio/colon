#!/bin/bash
echo "🎫 Installing Colón..."

# Pull the image
docker pull strucio/colon:latest

# Create .env file template
cat > .env << EOF
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your-webhook-url
TEST_MODE=false
EOF

echo "✅ Installation complete!"
echo "📝 Edit .env file with your Discord webhook URL"
echo "🚀 Run with: docker run -d --name colon --env-file .env strucio/colon:latest"
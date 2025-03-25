#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Make sure the .env file exists
if [ ! -f ".env" ]; then
    echo "Creating .env file..."
    echo "TOKEN=your_discord_token" > .env
    echo "GUILD_ID=your_guild_id" >> .env
    echo "Please update the .env file with your actual Discord token and Guild ID"
fi

# Start the bot
echo "Starting Eagle2 Discord bot..."
python main.py

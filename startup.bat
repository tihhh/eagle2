@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo Checking for .env file...
if not exist .env (
    echo Creating .env file template...
    echo TOKEN=your_discord_token > .env
    echo GUILD_ID=your_guild_id >> .env
    echo Please update the .env file with your actual Discord token and Guild ID
)

echo Starting Eagle2 Discord bot...
python main.py

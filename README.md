
# Discord AI Bot

This project is a Discord bot that can join voice channels, record audio for a specified duration, process the recorded audio, and send API requests to generate text responses. The bot can also play these text responses as audio back in the voice channel. Additionally, it supports various slash commands for interaction.

## Features

- Joins voice channels in a Discord server.
- Records audio and converts it to text.
- Sends API requests based on the transcribed text and retrieves responses.
- Plays the API response as audio in the voice channel.
- Supports slash commands for easy interaction.

## Installation

1. Clone this repository or download the zip file:

    ```bash
    git clone https://github.com/yourusername/discord-ai-bot.git
    cd discord-ai-bot
    ```

2. Install the required Python packages using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project root directory and add your Discord bot token and application ID:

    ```
    DISCORD_TOKEN=your_discord_bot_token
    DISCORD_APP_ID=your_discord_application_id
    ```

4. Run the bot:

    ```bash
    python bot.py
    ```

## Usage

### Slash Commands

- `/join` - Invites the bot to join your current voice channel.
- `/leave` - Commands the bot to leave the current voice channel.
- `/listen` - Records audio from the voice channel for a specified duration (in seconds) and processes the audio.
- `/help` - Displays the help menu with all available commands.

## Project Structure

```
discord-ai-bot/
│
├── bot.py               # Main bot file to run the bot
├── commands/
│   ├── __init__.py      # Initializes the commands package
│   ├── join.py          # /join command
│   ├── leave.py         # /leave command
│   ├── listen.py        # /listen command
│   └── help.py          # /help command
├── utils/
│   ├── __init__.py      # Initializes the utils package
│   ├── audio.py         # Audio processing utilities
│   ├── api.py           # API request utilities
│   └── microphone.py    # Microphone-related utilities
├── .env                 # Environment variables (not included in the repo)
├── requirements.txt     # Python package requirements
└── README.md            # Project documentation
```

## Dependencies

- Python 3.10+
- `discord.py` - Discord API wrapper for Python
- `requests` - To handle API requests
- `gtts` - Google Text-to-Speech for generating audio from text
- `speechrecognition` - For speech-to-text processing
- `python-dotenv` - For loading environment variables from a `.env` file

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

# Main configuration file

# Mandatory Variables
API_ID = 23171051 # Replace with your actual Telegram API ID
API_HASH = "10331d5d712364f57ffdd23417f4513c"  # Replace with your actual Telegram API Hash
BOT_TOKEN = "7569956429:AAEnSX4FNm4_8CsQ_IPdIp8T93_nQ4JqesI"  # Replace with your actual Bot Token
OWNER_ID = "6987799874"  # Replace with your actual Owner ID
# Database
DATABASE_URL = "mongodb+srv://tmrbotz:gRkWfPA0ToDRNe1d@cluster0.rxoovko.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your actual database URL

AUTH_CHAT = "-1002234850464" # Replace with your actual auth chat ID. You can use multiple IDs separated by ( space ).
LOGS_CHAT = -1002205504138 # Replace with your actual logs chat ID
POST_CHAT = -1002205504138 # Replace with your actual post chat ID

ADMIN_USERNAME = "admin" # Replace with your admin username
ADMIN_PASSWORD = "vishal" # Replace with your admin password


SITE_SECRET = "Tmrbotz*12345" # Replace with your site secret key
TMDB_API_KEY = "4b6e108d2d340e1c4da27a739feaf820" # Replace with your TMDB API key

# Optional Variables

# If you want to use multiple bot tokens, uncomment the MULTI_TOKENS dictionary and add your tokens. this aditional bots will speed up the process of downloading and streaming files.
MULTI_TOKENS = {
    # 1: "BOT_TOKEN_1_HERE",
    # 2: "BOT_TOKEN_2_HERE",
    # Add more tokens as needed
}
DELETE_AFTER_MINUTES = 10 # Set the number of minutes after which files will be deleted from user message
POST_UPDATES = False # Set to True if you want to post updates in the post chat
USE_CAPTION = False # Set to True if you want to use captions for posts instead of file names.

# Port configuration
import os
PORT = int(os.environ.get("PORT", 6519))
















# (Don't touch this unless you know what you're doing)
SUDO_USERS = [int(x) for x in (OWNER_ID).split()]
AUTH_CHATS = [int(x) for x in (AUTH_CHAT).split()]

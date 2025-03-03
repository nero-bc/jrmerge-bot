
import os

class Config(object):
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = os.environ.get("API_ID")
    OWNER = os.environ.get("OWNER")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    OWNER_NAME = os.environ.get("OWNER_NAME", "StupidBoi69")
    PASSWORD = os.environ.get("PASSWORD")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    LOGCHANNEL = os.environ.get("LOGCHANNEL")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    
    IS_PREMIUM = os.environ.get("IS_PREMIUM")
    PAID_BOT = os.environ.get("PAID_BOT")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    SHORTENER_SITE = os.environ.get("SHORTENER_SITE")
    SHORTENER_API = os.environ.get("SHORTENER_API")

    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]

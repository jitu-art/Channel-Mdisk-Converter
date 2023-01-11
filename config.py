import os

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "27053003"))
API_HASH = os.environ.get("API_HASH", "b5fa36b05e1bf25719a7586bb9ecf0f4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5698225715:AAF72ftiVMTPXK5-wL9CAIkluBqhf41_B7w")
DROPLINK_API = os.environ.get("DROPLINK_API")
MDISK_API = os.environ.get("MDISK_API", "y6aUZNtr9JsnZ9MsVejf")
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split("1355978729")) if os.environ.get("ADMINS") else []
DATABASE_NAME = os.environ.get("DATABASE_NAME", "MdiskConvertorBotpro")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongosh "mongodb+srv://cluster0.skivirl.mongodb.net/myFirstDatabase" --apiVersion 1 --username jivtubot")
WEBSITE = os.environ.get('WEBSITE')

#  Optionnal variables
INCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("INCLUDE_DOMAIN").split(",")) if os.environ.get("INCLUDE_DOMAIN") else []
EXCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("EXCLUDE_DOMAIN").split(",")) if os.environ.get("EXCLUDE_DOMAIN") else []
CHANNELS = is_enabled((os.environ.get('CHANNELS', "True")), True)
CHANNEL_ID = list(int(i.strip()) for i in os.environ.get("-1001836860485").split("-1001836860485")) if os.environ.get("-1001836860485") else []
FORWARD_MESSAGE = is_enabled((os.environ.get('FORWARD_MESSAGE', "True")), True)
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://github.com/CyniteOfficial/Channel-Mdisk-Converter")
USERNAME = os.environ.get("USERNAME", "CyniteBackup")
HEADER_TEXT = os.environ.get("HEADER_TEXT", '')
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", '')
BANNER_IMAGE = os.environ.get("BANNER_IMAGE", '')
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = is_enabled((os.environ.get('LINK_BYPASS', "False")), False)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU = True if HEROKU_API_KEY and HEROKU_APP_NAME else False

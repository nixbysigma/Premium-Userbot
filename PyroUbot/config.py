import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "999"))

DEVS = list(map(int, os.getenv("DEVS", "7463774265").split()))

API_ID = int(os.getenv("API_ID", "21825364"))

API_HASH = os.getenv("API_HASH", "f268e8cdb0728ee658d8e5cba3464cb0")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8150379277:AAFdCxFrnJi84QpeAWIcTXjIMBSjEo-Nyo4")

OWNER_ID = int(os.getenv("OWNER_ID", "7463774265"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", " -1002356932965").split()))

RMBG_API = os.getenv("RMBG_API", "f3CYy31QTGdSyYABY8D7FTqQ")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Unixxpedia:unix2008@cluster0.cn4kypa.mongodb.net/Unixxpedia?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002552768474"))

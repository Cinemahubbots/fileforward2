import os
from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", 22359038))
    API_HASH = environ.get("API_HASH", "b3901895dc193c30c808ba4f1b550ed0")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = ""
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = environ.get("BOT_OWNER", "5531461861")

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '13126185'))
    API_HASH = str(getenv('API_HASH', '945d34fcce68f4bffc600fa702ca1506'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5539483502:AAEGjwRwBNOEBhjrEiDblgAfcddcIyz6_y0'))
    name = str(getenv('SESSION_NAME', 'File-To-Link'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    PREMIUM_USERS = set(int(premium) for premium in os.environ.get("PREMIUM_USERS", "1004846223 1602928828 1959758830 942099709 5289350909 493632262 5062213900 1022415852 1302417752").split()) 
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001436214747'))
    PORT = int(getenv('PORT', 8080))
    WAIT_TIME = int(getenv('WAIT_TIME', 300))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "942099709").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', '@kwic2002'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'kwicishere.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://kwicbot:kwicbot@cluster0.frltr.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'MoviesNowOTT2'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 

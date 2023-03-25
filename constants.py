import os
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()
LOGIN_INTERVAL = float(os.environ["LOGIN_INTERVAL"])
_ = int(os.environ["_"])
Q__A = True if os.environ["Q__A"] == "True" else False
Q__B = True if os.environ["Q__B"] == "True" else False
Q__C = True if os.environ["Q__C"] == "True" else False
Q__D = True if os.environ["Q__D"] == "True" else False
Q__E = True if os.environ["Q__E"] == "True" else False
Q__F = True if os.environ["Q__F"] == "True" else False
Q__G = True if os.environ["Q__G"] == "True" else False
_MIN = float(os.environ["_MIN"])
_MAX = float(os.environ["_MAX"])
TOTAL__MAX = float(os.environ["TOTAL__MAX"])
LOOP = int(os.environ["LOOP"])
_MAX = int(os.environ["_MAX"])
BASIC_ = int(os.environ["BASIC_"])
WAITING_INTERVAL = float(os.environ["WAITING_INTERVAL"])
RELEASING_INTERVAL = float(os.environ["RELEASING_INTERVAL"])
LIMITATION = True if os.environ["LIMITATION"] == "True" else False
START_TIME = int(os.environ["START_TIME"])
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
SLACK_URL = os.environ["SLACK_URL"]
SLACK_CHANNEL_RESULT = os.environ["SLACK_CHANNEL_RESULT"]
SLACK_CHANNEL_LOG = os.environ["SLACK_CHANNEL_LOG"]
_URL = os.environ["_URL"]
_ID = os.environ["_ID"]
_PASSWORD = os.environ["_PASSWORD"]
_SWITCH = True if os.environ["_SWITCH"] == "True" else False
CHROMEDRIVER_PATH = os.environ["CHROMEDRIVER_PATH"]

from dotenv import load_dotenv
import os

load_dotenv()
TG_TOKEN = os.getenv("TG_TOKEN")
BASE_URL = f'https://api.telegram.org/bot{TG_TOKEN}'
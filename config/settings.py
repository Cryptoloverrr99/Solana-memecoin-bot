import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    TELEGRAM_TOKEN = os.getenv("8048350512:AAGVN4uZEt_D1q-ycNN6jhRo-PMn64ZHgiI")
    PUMPFUN_API_KEY = os.getenv("PUMPFUN_API_KEY")
    DEXSCREENER_API_KEY = os.getenv("DEXSCREENER_API_KEY")

settings = Settings()

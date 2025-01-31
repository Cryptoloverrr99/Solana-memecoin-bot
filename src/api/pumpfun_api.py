import requests
from config import settings

PUMPFUN_API = "https://api.pump.fun/v1/migrations"  # API hypothétique

def check_pumpfun_migrations():
    try:
        response = requests.get(PUMPFUN_API, params={"network": "solana"})
        return response.json().get('migrations', [])
    except Exception as e:
        raise Exception(f"API Pump.fun indisponible : {str(e)}")

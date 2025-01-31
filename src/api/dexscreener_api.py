import requests
from config.settings import settings

def get_dexscreener_data(token_address: str):
    """
    Récupère les données d'un token depuis Dexscreener.
    Exemple d'endpoint : https://api.dexscreener.com/v1/tokens/{token_address}
    """
    try:
        url = f"https://api.dexscreener.com/v1/tokens/{token_address}"
        headers = {"Authorization": f"Bearer {settings.DEXSCREENER_API_KEY}"}  # Si une clé est requise
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # Extraction des données pertinentes (ajustez selon la réponse de l'API)
        return {
            "price": data["pairs"][0]["priceUsd"],
            "liquidity": data["pairs"][0]["liquidity"]["usd"],
            "holders": data["pairs"][0]["holders"],
            "is_trending": data["pairs"][0]["txns"]["h24"] > 1000  # Exemple de condition "trending"
        }
    except Exception as e:
        raise Exception(f"Erreur Dexscreener : {str(e)}")

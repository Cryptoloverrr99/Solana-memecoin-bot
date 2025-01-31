import requests

def get_dexscreener_data(token_address: str):
    """
    Récupère les données d'un token depuis Dexscreener.
    """
    endpoint = f"https://api.dexscreener.com/v1/tokens/{token_address}"
    try:
        response = requests.get(endpoint)
        data = response.json()
        
        # Vérifie si des paires existent
        if not data.get("pairs"):
            return {"error": "Aucune paire trouvée pour ce token."}
        
        # Prend la première paire (la plus liquide)
        pair = data["pairs"][0]
        
        return {
            "price": pair.get("priceUsd", 0),
            "liquidity": pair.get("liquidity", {}).get("usd", 0),
            "holders": pair.get("holders", 0),
            "url": pair.get("url", ""),
            "symbol": pair.get("baseToken", {}).get("symbol", "N/A")
        }
    except Exception as e:
        return {"error": f"Erreur API Dexscreener: {str(e)}"}

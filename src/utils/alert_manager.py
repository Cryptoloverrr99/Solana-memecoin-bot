def send_alert(bot, coin_data, chat_id):
    dex_data = get_dexscreener_data(coin_data["token_address"])
    message = f"""
    📊 **DEXSCREENER UPDATE** 📊
    Prix actuel : ${dex_data['price']}
    Liquidité 24h : ${dex_data['liquidity']}
    """
    bot.send_message(...)

def send_alert(bot, coin_data, chat_id):
    message = f"""
    🚨 **Alerte Migration** 🚨
    ---------------------
    **Nom**: {coin_data.get('name', 'N/A')}
    **Symbol**: {coin_data.get('symbol', 'N/A')}
    **Market Cap**: ${coin_data.get('market_cap', 0):,.2f}
    **Liquidité**: ${coin_data.get('liquidity', 0):,.2f}
    **Holders**: {coin_data.get('holders', 0)}
    **Score Social**: {coin_data.get('social_score', 0)}/100
    **Lien**: [DexScreener]({coin_data.get('dexscreener_url', '#')})
    """
    bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")

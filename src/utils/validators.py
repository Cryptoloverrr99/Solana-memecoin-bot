def validate_conditions(coin_data):
    conditions = [
        coin_data.get('market_cap', 0) > 100000,
        coin_data.get('dev_holding', 1) <= 0.10,
        not coin_data.get('dev_sold', False),
        coin_data.get('dex_paid', False),
        coin_data.get('top10_holders', 1) <= 0.20,
        coin_data.get('liquidity', 0) >= 80000,
        coin_data.get('holders', 0) >= 500,
        coin_data.get('social_score', 0) >= 50,
        coin_data.get('is_trending', False)
    ]
    return all(conditions)

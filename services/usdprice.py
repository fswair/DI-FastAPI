from requests import get

def get_usd_price() -> float:
    """
    Fetch the current USD price from an external API.
    """
    try:
        response = get('https://api.exchangerate-api.com/v4/latest/USD')
        response.raise_for_status()
        data = response.json()
        if not data or 'rates' not in data:
            raise ValueError("Invalid response from API")
        return data.get('rates', {}).get('TRY', 0.0)
    except Exception as e:
        print(f"Error fetching USD price: {e}")
        return 0.0
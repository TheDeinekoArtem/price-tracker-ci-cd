from datetime import datetime, timedelta
from price_tracker import read_price_data

def get_price_change(product_name: str, file_path: str, days: int = 30) -> tuple[float, float] | None:
    """Повертає початкову та кінцеву ціну товару за останні 'days' днів."""
    price_data = read_price_data(file_path)
    product_prices = [(date, price) for name, date, price in price_data if name == product_name]

    if not product_prices:
        return None

    product_prices.sort(key=lambda x: x[0])  # Сортуємо за датою
    cutoff_date = datetime.now() - timedelta(days=days)
    last_month_prices = [price for date, price in product_prices if date >= cutoff_date]

    if len(last_month_prices) < 2:
        return None

    return last_month_prices[0], last_month_prices[-1]
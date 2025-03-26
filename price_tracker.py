from datetime import datetime, timedelta


def read_price_data(file_path: str) -> list:
    """Зчитує дані з файлу та повертає список кортежів (назва, дата, ціна)."""
    price_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            name, date_str, price = line.strip().split(',')
            date = datetime.strptime(date_str, '%Y-%m-%d')
            price_data.append((name, date, float(price)))
    return price_data


def get_price_change(
    product_name: str,
    file_path: str,
    days: int = 30
) -> tuple[float, float] | None:
    """Повертає початкову та кінцеву ціну товару за останні 'days' днів.
    """
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


if __name__ == "__main__":
    result = get_price_change("apple", "prices.txt")
    if result:
        start_price, end_price = result
        print(f"Початкова ціна: {start_price}, Кінцева ціна: {end_price}, "
              f"Зміна: {end_price - start_price}")
    else:
        print("Недостатньо даних для товару.")

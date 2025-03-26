from datetime import datetime, timedelta
from get_price_change import get_price_change

def read_price_data(file_path: str) -> list:
    """Зчитує дані з файлу та повертає список кортежів (назва, дата, ціна)."""
    price_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            name, date_str, price = line.strip().split(',')
            date = datetime.strptime(date_str, '%Y-%m-%d')
            price_data.append((name, date, float(price)))
    return price_data

if __name__ == "__main__":
    result = get_price_change("apple", "prices.txt")
    if result:
        start_price, end_price = result
        print(f"Початкова ціна: {start_price}, Кінцева ціна: {end_price}, Зміна: {end_price - start_price}")
    else:
        print("Недостатньо даних для товару.")
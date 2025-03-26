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
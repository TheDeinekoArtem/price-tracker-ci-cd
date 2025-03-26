import pytest
from datetime import datetime
from price_tracker import read_price_data

@pytest.fixture
def sample_file(tmp_path):
    """Фікстура для створення тимчасового файлу з тестовими даними."""
    file = tmp_path / "test_prices.txt"
    file.write_text(
        "apple,2025-02-25,10.5\n"
        "apple,2025-03-10,11.0\n"
        "apple,2025-03-25,12.0\n"
        "banana,2025-03-20,6.0\n"
    )
    return str(file)

def test_read_price_data(sample_file):
    """Тестування функції read_price_data."""
    data = read_price_data(sample_file)
    assert len(data) == 4
    assert data[0] == ("apple", datetime(2025, 2, 25), 10.5)
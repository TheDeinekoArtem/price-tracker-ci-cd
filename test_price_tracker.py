import pytest
from datetime import datetime
from price_tracker import read_price_data, get_price_change


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


@pytest.mark.parametrize(
    "product_name, expected_result",
    [
        ("apple", (10.5, 12.0)),  # Зміна ціни за місяць
        ("banana", None),         # Недостатньо даних
        ("orange", None),         # Товару немає
    ]
)
def test_get_price_change(sample_file, product_name, expected_result):
    """Тестування функції get_price_change з параметризацією."""
    result = get_price_change(product_name, sample_file, days=30)
    assert result == expected_result

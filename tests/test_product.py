import pytest

from src.product import Product


# Фикстура для создания первого продукта
@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000, quantity=5
    )


# Фикстура для создания второго продукта
@pytest.fixture
def second_product():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000, quantity=8)


# Тесты для проверки создания продукта
def test_product_creation(first_product):
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000
    assert first_product.quantity == 5


# Тесты для проверки атрибутов продукта
def test_product_attributes(first_product):
    assert isinstance(first_product.name, str)
    assert isinstance(first_product.description, str)
    assert isinstance(first_product.price, (int, float))
    assert isinstance(first_product.quantity, int)


# Фикстура для подтверждения ввода
@pytest.fixture
def confirmation_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")


# Тесты для проверки установки положительной цены
def test_price_setter_positive(first_product, confirmation_input):
    first_product.price = 150000
    assert first_product.price == 150000


# Тесты для проверки попытки установки отрицательной цены
def test_price_setter_negative(first_product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    first_product.price = -5000
    assert first_product.price == 180000  # Цена не должна измениться


# Тесты для проверки попытки установки нулевой цены
def test_price_setter_zero(first_product):
    first_product.price = 0
    assert first_product.price == 180000  # Цена не должна измениться


# Тесты для проверки установки более низкой цены с подтверждением
def test_price_setter_lower_confirmed(first_product, confirmation_input):
    first_product.price = 160000  # Новая цена
    assert first_product.price == 160000


# Тесты для проверки сложения продуктов
def test_product_addition(first_product, second_product):
    assert first_product + second_product == 2580000  # 180000 * 5 + 210000 * 8 = 2580000

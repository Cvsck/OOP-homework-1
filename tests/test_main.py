import pytest

from src.main import Category, Product


# Фикстура для создания первого продукта
@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000, quantity=5
    )


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


# Фикстура для создания первой категории
@pytest.fixture
def first_category():
    Category.category_count = 0  # Сбросить значение переменной класса перед тестами
    Category.product_count = 0

    product4 = Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000, quantity=7)

    return Category(
        name="Телевизоры",
        description=(
            "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
        ),
        products=[product4],
    )


# Тесты для проверки создания категории
def test_category_creation(first_category):
    assert first_category.name == "Телевизоры"
    assert first_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, " "станет вашим другом и помощником"
    )
    assert first_category.products[0].name == '55" QLED 4K'


# Тесты для проверки атрибутов категории
def test_category_attributes(first_category):
    assert isinstance(first_category.name, str)
    assert isinstance(first_category.description, str)
    assert isinstance(first_category.products, list)
    assert all(isinstance(product, Product) for product in first_category.products)


# Тесты для проверки счетчиков категории и продукта
def test_category_and_product_count(first_category):
    assert Category.category_count == 1
    assert Category.product_count == 1

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000, 8)
    category2 = Category(
        "Смартфоны",
        (
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        [product1, product2],
    )

    assert category2.name == "Смартфоны"
    assert category2.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получения дополнительных функций для удобства жизни"
    )
    assert len(category2.products) == 2

    assert Category.category_count == 2
    assert Category.product_count == 3


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

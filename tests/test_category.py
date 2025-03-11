import pytest

from src.category import Category
from src.product import Product


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
    assert first_category.get_products()[0].name == '55" QLED 4K'  # Используем метод get_products()


# Тесты для проверки атрибутов категории
def test_category_attributes(first_category):
    assert isinstance(first_category.name, str)
    assert isinstance(first_category.description, str)
    assert isinstance(first_category.get_products(), list)  # Используем метод get_products()
    assert all(isinstance(product, Product) for product in first_category.get_products())


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
    assert len(category2.get_products()) == 2  # Используем метод get_products()

    assert Category.category_count == 2
    assert Category.product_count == 3

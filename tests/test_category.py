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


# Тесты для метода middle_price
def test_middle_price_no_products():
    # Создание категории без продуктов
    empty_category = Category(name="Пустая категория", description="Нет продуктов в категории")

    # Проверка обработки исключения и возврата 0
    assert empty_category.middle_price() == 0


def test_middle_price_with_products(first_category):
    # Проверка расчёта средней цены с использованием первой категории
    assert first_category.middle_price() == 123000.0

    # Добавляем ещё один продукт в категорию
    product2 = Product(name="SmartTV", description="Описание", price=77000, quantity=10)
    first_category.add_product(product2)

    # Проверяем среднюю цену после добавления продукта
    expected_average_price = (123000 + 77000) / 2  # Средняя цена продуктов
    assert first_category.middle_price() == expected_average_price


# Тест на добавление некорректного продукта
def test_add_invalid_product():
    category = Category(name="Некорректные продукты", description="Категория для тестирования")

    # Проверка добавления не-продукта вызывает TypeError
    with pytest.raises(TypeError):
        category.add_product("Некорректный продукт")  # Ожидается TypeError


# Тесты для проверки счетчиков категории и продукта с новым методом
def test_category_and_product_count_with_middle_price():
    Category.category_count = 0  # Сбросить значение переменной класса перед тестами
    Category.product_count = 0

    product1 = Product(name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет", price=180000, quantity=5)
    product2 = Product(name="Iphone 15", description="512GB, Gray space", price=210000, quantity=8)

    category = Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        products=[product1, product2],
    )

    # Проверяем среднюю цену
    expected_average_price = (180000 + 210000) / 2
    assert category.middle_price() == expected_average_price

    # Проверяем счетчики категорий и продуктов
    assert Category.category_count == 1
    assert Category.product_count == 2

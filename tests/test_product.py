import pytest
from src.product import Smartphone
from tests.config import first_product, second_product, smartphone, lawn_grass, category


# Тест на проверку создания базового продукта
def test_product_creation(first_product):
    """Проверяем, что объект продукта first_product создаётся с правильными атрибутами."""
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000
    assert first_product.quantity == 5


# Тест для проверки типов атрибутов продукта
def test_product_attributes(first_product):
    """Проверяем, что атрибуты продукта имеют правильные типы данных."""
    assert isinstance(first_product.name, str)
    assert isinstance(first_product.description, str)
    assert isinstance(first_product.price, (int, float))
    assert isinstance(first_product.quantity, int)


@pytest.fixture
def confirmation_input(monkeypatch):
    """Эмулируем пользовательский ввод 'y' (подтверждение)."""
    monkeypatch.setattr("builtins.input", lambda _: "y")


# Тест на установку новой положительной цены
def test_price_setter_positive(first_product, confirmation_input):
    """Проверяем установку новой положительной цены."""
    first_product.price = 150000
    assert first_product.price == 150000


# Тест на попытку установить отрицательную цену
def test_price_setter_negative(first_product, monkeypatch):
    """Проверяем защиту от установки отрицательной цены."""
    monkeypatch.setattr("builtins.input", lambda _: "n")  # Эмулируем отказ от изменения цены
    first_product.price = -5000
    assert first_product.price == 180000  # Цена не должна измениться


# Тест на попытку установить нулевую цену
def test_price_setter_zero(first_product):
    """Проверяем защиту от установки нулевой цены."""
    first_product.price = 0
    assert first_product.price == 180000  # Цена не должна измениться


# Тест на подтверждённое снижение цены
def test_price_setter_lower_confirmed(first_product, confirmation_input):
    """Проверяем подтверждённое снижение цены продукта."""
    first_product.price = 160000  # Устанавливаем новую цену ниже текущей
    assert first_product.price == 160000


# Тест на сложение двух продуктов
def test_product_addition(first_product, second_product):
    """Проверяем корректность сложения двух продуктов."""
    assert first_product + second_product == 2580000  # 180000 * 5 + 210000 * 8


# Тест на создание смартфона
def test_smartphone_creation(smartphone):
    """Проверяем, что объект смартфона создаётся с правильными атрибутами."""
    assert smartphone.name == "Iphone 15"
    assert smartphone.description == "512GB, Gray space"
    assert smartphone.price == 210000.0
    assert smartphone.quantity == 8
    assert smartphone.efficiency == 98.2
    assert smartphone.model == "15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray space"


# Тест на создание газонной травы
def test_lawn_grass_creation(lawn_grass):
    """Проверяем, что объект газонной травы создаётся с правильными атрибутами."""
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 7
    assert lawn_grass.color == "Зеленый"


# Тест на сложение объектов одного класса (например, смартфонов)
def test_addition_same_class(smartphone):
    """Проверяем сложение двух объектов класса Smartphone."""
    smartphone2 = Smartphone(
        name="Samsung Galaxy S22",
        description="256GB, Черный",
        price=70000,
        quantity=3,
        efficiency=90.0,
        model="S22",
        memory=256,
        color="Черный",
    )
    assert smartphone + smartphone2 == (210000.0 * 8) + (70000 * 3)


# Тест на ошибку при сложении разных классов (смартфона и газонной травы)
def test_addition_different_classes(smartphone, lawn_grass):
    """Проверяем, что сложение объектов разных классов вызывает TypeError."""
    with pytest.raises(TypeError):
        smartphone + lawn_grass


# Тест на добавление продуктов в категорию
def test_add_product_to_category(category, smartphone, lawn_grass):
    """Проверяем, что можно добавить корректные продукты в категорию."""
    category.add_product(smartphone)
    category.add_product(lawn_grass)
    assert smartphone in category.get_products()
    assert lawn_grass in category.get_products()


# Тест на добавление некорректного объекта в категорию
def test_invalid_product_addition(category):
    """Проверяем, что добавление некорректного объекта вызывает TypeError."""
    with pytest.raises(TypeError):
        category.add_product("Некорректный объект")  # Ожидается ошибка TypeError

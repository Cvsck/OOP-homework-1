import pytest

from src.product import LawnGrass, Product, Smartphone


# Тест на проверку создания базового продукта
def test_product_creation(capsys):
    first_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5)
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000
    assert first_product.quantity == 5

    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out


# Тест для проверки типов атрибутов продукта
def test_product_attributes():
    product = Product("Test Product", "Описание", 1500.0, 10)
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, (int, float))
    assert isinstance(product.quantity, int)


@pytest.fixture
def confirmation_input(monkeypatch):
    """Эмулируем пользовательский ввод 'y' (подтверждение)."""
    monkeypatch.setattr("builtins.input", lambda _: "y")


# Тесты на price setter
def test_price_setter_positive(confirmation_input):
    product = Product("Test Product", "Описание", 1500.0, 10)
    product.price = 1000.0
    assert product.price == 1000.0


def test_price_setter_negative():
    product = Product("Test Product", "Описание", 1500.0, 10)
    product.price = -500
    assert product.price == 1500.0  # Цена не изменилась


# Тест на сложение продуктов
def test_product_addition():
    product1 = Product("Product 1", "Описание", 1500.0, 10)
    product2 = Product("Product 2", "Описание", 2000.0, 5)
    assert product1 + product2 == (1500 * 10) + (2000 * 5)


# Тест на создание смартфона
def test_smartphone_creation(capsys):
    smartphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "15", 512, "Gray space")
    assert smartphone.name == "Iphone 15"
    assert smartphone.model == "15"
    captured = capsys.readouterr()
    assert "Создан объект класса Smartphone" in captured.out


# Тест на создание газонной травы
def test_lawn_grass_creation(capsys):
    lawn_grass = LawnGrass("Газонная трава", "Описание", 500, 20, "Россия", 7)
    assert lawn_grass.name == "Газонная трава"
    captured = capsys.readouterr()
    assert "Создан объект класса LawnGrass" in captured.out

import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000, quantity=5
    )


@pytest.fixture
def second_product():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000, quantity=8)


@pytest.fixture
def smartphone():
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )


@pytest.fixture
def lawn_grass():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500,
        quantity=20,
        country="Россия",
        germination_period=7,
        color="Зеленый",
    )


@pytest.fixture
def category():
    return Category(name="Смартфоны", description="Высокотехнологичные устройства", products=[])

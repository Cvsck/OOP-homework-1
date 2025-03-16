from abc import ABC, abstractmethod


# Базовый абстрактный класс
class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirm = input(f"Цена понижается с {self.__price} до {value}. Вы уверены? (y/n): ")
            if confirm.lower() == "y":
                self.__price = value
                print(f"Цена изменена на {value}")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = value

    @abstractmethod
    def calculate_total_price(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


# Миксин для логирования создания объектов
class InitLoggingMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        print(f"Создан объект класса {class_name} с аргументами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.__dict__})>"


# Класс продуктов с миксином
class Product(InitLoggingMixin, BaseProduct):
    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        return self.price * self.quantity + other.price * other.quantity


# Класс смартфонов
class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, model: str, memory: int, color: str):
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{super().__str__()}, Модель: {self.model}, Память: {self.memory} ГБ, Цвет: {self.color}"


# Класс газонной травы
class LawnGrass(Product):
    def __init__(
        self, name: str, description: str, price: float, quantity: int, country: str, germination_period: int
    ):
        self.country = country
        self.germination_period = germination_period
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{super().__str__()}, Страна: {self.country}, Период прорастания: {self.germination_period} дней"


# Класс для категории продуктов
class ProductCategory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                f"Можно добавлять только объекты класса Product и его наследников, а не {type(product).__name__}"
            )
        self.products.append(product)

    def get_products(self):
        return self.products

    def __str__(self):
        return "\n".join(str(product) for product in self.products)

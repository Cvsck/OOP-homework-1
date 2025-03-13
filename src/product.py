class Product:
    name: str
    description: str
    __price: float  # Приватный атрибут
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
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

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        if type(self) != type(other):  # Проверка типов
            raise TypeError(f"Нельзя складывать объекты разных типов: {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        return f"{super().__str__()}, Модель: {self.model}, Цвет: {self.color}, Память: {self.memory} ГБ, Производительность: {self.efficiency}"


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        return f"{super().__str__()}, Страна: {self.country}, Период прорастания: {self.germination_period} дней, Цвет: {self.color}"


class ProductCategory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):  # Проверка через isinstance
            raise TypeError(
                f"Можно добавлять только объекты класса Product и его наследников, а не {type(product).__name__}"
            )
        self.products.append(product)

    def __str__(self):
        return "\n".join(str(product) for product in self.products)

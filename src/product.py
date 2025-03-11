class Product:
    name: str
    description: str
    __price: float  # Полностью приватный атрибут
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price  # Инициализация приватного атрибута
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict, existing_products: list):
        # Поиск существующего товара по имени
        for product in existing_products:
            if product.name == product_dict["name"]:
                # Обновляем количество товара и выбираем более высокую цену
                product.quantity += product_dict["quantity"]
                product.price = max(product.price, max(0, product_dict["price"]))  # Учитываем отрицательную цену
                return product

        # Создаем новый товар, если такого еще нет
        return cls(**product_dict)  # Использование ** для распаковки словаря

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

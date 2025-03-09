class Product:
    name: str
    description: str
    _price: float  # Приватный атрибут
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self._price = price  # Инициализация приватного атрибута
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
        return cls(
            name=product_dict["name"],
            description=product_dict["description"],
            price=max(0, product_dict["price"]),  # Устанавливаем цену равной нулю, если она отрицательная
            quantity=product_dict["quantity"],
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self._price:
            confirm = input(f"Цена понижается с {self._price} до {value}. Вы уверены? (y/n): ")
            if confirm.lower() == "y":
                self._price = value
                print(f"Цена изменена на {value}")
            else:
                print("Изменение цены отменено")
        else:
            self._price = value


class Category:
    name: str
    description: str
    __products: list  # Приватный атрибут
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []

        # Увеличение значения атрибутов класса
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> list:
        return self.__products

    @property
    def products_as_string(self) -> str:
        return "\n".join([f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products])

    def get_products(self) -> list:
        return self.__products


# Пример использования
if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products_as_string)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products_as_string)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        },
        category1.get_products(),
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100  # Выведет сообщение и значение не будет изменено
    print(new_product.price)
    new_product.price = 0  # Выведет сообщение и значение не будет изменено
    print(new_product.price)
    new_product.price = 170000  # Запрос на подтверждение уменьшения цены
    print(new_product.price)

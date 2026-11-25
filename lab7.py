# Создаём класс Product
class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    # Вычисление общей стоимости товара
    def get_total(self):
        return self.price * self.quantity

    # Вычисление стоимости со скидкой
    def get_discount(self, discount):
        total = self.get_total()
        return total - total * discount / 100

    # Вывод информации о товаре
    def show_info(self):
        print("Название:", self.name)
        print("Категория:", self.category)
        print("Цена:", self.price, "руб.")
        print("Количество:", self.quantity)
        print("Общая стоимость:", self.get_total(), "руб.")
        print("Стоимость со скидкой 10%:",
              round(self.get_discount(10), 2), "руб.")


# Создаём объект класса Product
product = Product("Ноутбук", "Электроника", 50000, 2)

# Выводим информацию о товаре
product.show_info()
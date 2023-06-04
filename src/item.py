import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только два объекта Item.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data = os.path.join(current_dir, 'items.csv')
        with open(data, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = cls(row['name'], float(row['price']), int(row['quantity']))
                cls.all.append(item)

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))

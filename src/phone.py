from src.item import Item


class Phone(Item):
    """`Phone` содержит все атрибуты класса `Item` и дополнительно атрибут,
    содержащий количество поддерживаемых сим - карт"""
    def __init__(self, name, price, quantity, number_of_sim: int) -> None:
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Дополнительный атрибут
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int):
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = number_of_sim

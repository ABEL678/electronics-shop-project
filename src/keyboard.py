from src.item import Item


class MixinLang:
    lang = "EN"

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def language(self):
        return self.lang

    def change_lang(self):
        if self.lang == "EN":
            self.lang = "RU"
        else:
            self.lang = "EN"


class Keyboard(MixinLang, Item):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavors):
        super().__init__(name, cuisine)
        self.flavors = flavors
    def show_flavors(self):
        print("Сорта:", ", ".join(self.flavors))
shop = IceCreamStand("Мороженоее", "Кафе", ["Ваниль", "Шоколад", "Фисташка"])
shop.show_flavors()
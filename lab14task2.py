class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavors, location, hours):
        super().__init__(name, cuisine)
        self.flavors = flavors
        self.location = location
        self.hours = hours
    def show(self):
        print(f"{self.name} | {self.location} | {self.hours}")
        print("Сорта:", ", ".join(self.flavors))
    def add(self, f):
        if f not in self.flavors:
            self.flavors.append(f)
            print(f"+ {f}")
    def remove(self, f):
        if f in self.flavors:
            self.flavors.remove(f)
            print(f"- {f}")
shop = IceCreamStand("Десерты", "Кафе", ["Ваниль"], "улица Катерников", "5-1")
shop.show()
shop.add("Ваниль")
shop.show()
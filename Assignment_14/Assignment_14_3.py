class Book:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price


obj = Book(500)
print("Initial Price:", obj.get_price())
obj.set_price(650)
print("Updated Price:", obj.get_price())

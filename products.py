from logging import raiseExceptions


class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self._active = True

    def get_qunatity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity

    def is_active(self):
        return True

    def deactivate(self):
        return self.is_active == False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy (self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            total_price = self.price * quantity
            return total_price
        else:
            raise Exception ("You cannot order more than we have in stock")


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()
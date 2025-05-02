class Product():
    """creating a class with the attributes of product name price and quantity, that
        updates everytime the buy function or set_quantity is executed ."""

    def __init__(self, name, price, quantity):
        """initializing only validated data for the store,
        refactored into functions that validate the initial values"""
        self._validate_name(name)
        self.name = name
        self._validate_price(price)
        self.price = price
        self._validate_quantity(quantity)
        self.quantity = quantity
        self._active = True

    def _validate_name(self, name):
        """playing around with different approaches to validate data"""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name can not be empty and needs to be a str")

    def _validate_price(self, price):
        """price has to be greater than 0"""
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError ("Price must be positive float")

    def _validate_quantity(self, quantity):
        """Quantity has to be greater than 0"""
        if not isinstance(quantity, int) or quantity<=0:
            raise ValueError("Quantity has to be greater 0")

    def get_quantity(self):
        """returns total quantity of product"""
        return self.quantity

    def set_quantity(self, quantity):
        """Resets the quantity and deactivates the product if quantity is 0"""
        self._validate_quantity(quantity)
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """returns the activation status"""
        return self._active

    def activate(self):
        """activating the product"""
        self._active = True
        print(f"{self.name} is active")

    def deactivate(self):
        """deactivating the product"""
        self._active = False
        print(f'{self.name} has been deactivated')

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy (self, quantity):
        """Check if the quantity in stock is sufficient and applies promotion if available.
        returns the total price for one product"""
        if self.quantity >= quantity:
            self.quantity -= quantity
            total_price = self.price * quantity
            return total_price
        raise ValueError("You cannot order more than we have in stock")



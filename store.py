class Store:
    def __init__(self, l_products):
        """initializing the product list"""
        self.l_products = l_products


    def add_product(self, product):
        """appending a product"""
        self.l_products.append(product)


    def remove_prodcut(self, product):
        """removing a product"""
        self.l_products.remove(product)


    def get_all_products(self):
        """get all active products"""
        active_product = []
        for product in self.l_products:
            if product.is_active():
                active_product.append(product)
        return active_product


    def order(self, shopping_list):
        """check the entity and reduce the quantity if possible
        return the final price"""
        total = 0
        for product, amount in shopping_list:
            if amount > product.quantity:
                raise ValueError(f"Not enough in stock")
            else:
                product.quantity -= amount
                total += product.price * amount

        return f"Order made! Total payment: {total} dollars."


    def get_total_quantity(self):
        total_amount = []
        for item in self.l_products:
            total_amount.append(item.quantity)
        return sum(total_amount)


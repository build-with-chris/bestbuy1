from itertools import product

import products
class Store():
    def __init__(self, l_products):
        self.l_products = l_products

    def add_product(self, product):
        self.l_products.append(product)

    def remove_prodcut(self, product):
        self.l_products.remove(product)

    def get_all_products(self):
        active_product = []
        for product in self.l_products:
            if product._active:
                active_product.append(product)
        return active_product

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return f'Order cost: {total_price} dollars.'

    def get_total_quantity(self):
        total_amount = []
        for item in self.l_products:
            total_amount.append(item.quantity)
        return sum(total_amount)


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))
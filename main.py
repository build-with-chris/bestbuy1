import products
import store
best_buy = None


def main():
    """depending on the users choice, the user can display, or buy items from the shop"""
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    global best_buy
    best_buy = store.Store(product_list)

    while True:
        user_input = display_menu()
        if user_input == 1:
            display_product_details()
        if user_input == 2:
            print(f"\nTotal amount: {best_buy.get_total_quantity()}\n")
        if user_input == 3:
            display_product_details()
            print("When you want to finish order, enter empty text.")
            shopping_list = []
            while True:
                product_num = input("Which product # do you want? ")
                product_quan = input("What amount do you want? ")
                if product_num == "":
                    if shopping_list == []:
                        break
                    else:
                        try:
                            print(best_buy.order(shopping_list))
                            break
                        except ValueError:
                            print("\nError while making order! Quantity larger than what exists")
                            break
                try:
                    product_name = best_buy.l_products[int(product_num) -1]
                    product_quan = int(product_quan)
                    shopping_list.append((product_name, product_quan))
                except TypeError:
                    print("Please enter valid input")
        if user_input == 4:
            print("Bye")
            break


def display_menu():
    """A simple shop menu as shown in Codio"""
    print(f'\n')
    print(f'   Store Menu\n'
          f'    ----------\n'
          f'1. List all products in store\n'
          f'2. Show total amount in store\n'
          f'3. Make an order\n'
          f'4. Quit\n')
    while True:
        try:
            user_input = int(input("Please choose a number: "))
            return user_input
        except Exception:
            print("please enter a valid number")


def display_product_details():
    """A for loop that handles the different specifications regarding quantity of the products"""
    print(f'    ----------')
    for i, product in enumerate(best_buy.get_all_products(), 1):
        print(f'{i}. {product.name:28}, Price: ${product.price:4}, Quantity: {product.quantity}')


if __name__ == "__main__":
    main()

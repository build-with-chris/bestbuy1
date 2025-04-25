import products
import store


def setup_store():
    """Setting up an initial store with three objects"""
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        products.Product("Google Pixel 7", price=500, quantity=250)
                        ]
    return store.Store(product_list)


def start(store_obj):
    """depending on the users choice, the user can display, or buy items from the shop"""
    while True:
        user_input = display_menu()
        if user_input == 1:
            display_product_details(store_obj)
        if user_input == 2:
            print(f"\nTotal amount: {store_obj.get_total_quantity()}\n")
        if user_input == 3:
            handle_shopping(store_obj)
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
        except ValueError:
            print("please enter a valid number")


def display_product_details(store_obj):
    """A for loop that handles the different specifications regarding quantity of the products"""
    print('    ----------')
    for i, product in enumerate(store_obj.get_all_products(), 1):
        print(f'{i}. {product.name:28}, Price: ${product.price:4}, Quantity: {product.quantity}')


def validate_shopping_list(product_quan, product_num, store_obj):
    """takes the user input and compares it to the product database. If there is no
    error, it will return product and quantity to be added to the shopping list."""
    try:
        active_products = store_obj.get_all_products()
        product_name = active_products[int(product_num) - 1]
        product_quan = int(product_quan)
        if product_quan > 0:
            return (product_name, product_quan)
        else:
             raise ValueError
    except(TypeError, ValueError):
        print("Please enter valid input")
    except IndexError:
        print("The product number is not available. Please choose another product")
    return None


def handle_shopping(store_obj):
    """display active products, take user input and check if product is valid and available.
    if so, the total price will be calculated and quantity adapted"""
    active_products = store_obj.get_all_products()
    if not active_products:
        print("We are sold out")
        return

    display_product_details(store_obj)
    print("When you want to finish order, enter empty text.")

    shopping_list = []

    while True:
        product_num = input("Which product # do you want? ")
        if product_num == "":
            break

        product_quan = input("What amount do you want? ")
        validated = validate_shopping_list(product_quan, product_num, store_obj)
        if validated:
            shopping_list.append(validated)

    if shopping_list:
        try:
            print(store_obj.order(shopping_list))
        except ValueError as e:
            print(f"Order failed: {e}")
    else:
        print("No products selected. Order cancelled.")


if __name__ == "__main__":
    BEST_BUY = setup_store()
    start(BEST_BUY)

products = {
    1: {
        'name': 'Americano',
        'price': 100
    },
    2: {
        'name': 'Cappuccino',
        'price': 130
    },
    3: {
        'name': 'Espresso',
        'price': 140
    }
}


def is_int(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True


def get_selected_product():
    for id, product in products.items():
        print(f"Enter {id} for {product['name']}")

    selected_product_id_string = input('Select a product: ')
    print()
    while not (is_int(selected_product_id_string) and int(selected_product_id_string) in products.keys()):
        print('Invalid input')
        selected_product_id_string = input('Select a product: ')
        print()

    selected_product_id = int(selected_product_id_string)
    selected_product = products[selected_product_id]

    print(f"You have selected {selected_product['name']}")
    print()
    return selected_product


def get_quantity():
    quantity_string = input('Enter quantity: ')
    print()
    while not (is_int(quantity_string) and int(quantity_string) > 0):
        print('Invalid input')
        quantity_string = input('Enter quantity: ')
        print()

    quantity = int(quantity_string)
    return quantity


def get_order_item():
    selected_product = get_selected_product()
    quantity = get_quantity()

    order_item = selected_product.copy()
    order_item['quantity'] = quantity
    order_item['price'] *= order_item['quantity']

    return order_item


def ask_to_add_order_item():
    print('Enter 1 for NO')
    print('Enter 2 for YES')

    user_input = input('Would you like to order another item? ')
    print()
    while not (is_int(user_input) and int(user_input) in [1, 2]):
        print('Invalid input')
        user_input = input('Would you like to order another item? ')
        print()

    return bool(int(user_input)-1)


def group_order_items(order_items):
    grouped_order_items = {}

    for order_item in order_items:
        name = order_item['name']
        if name in grouped_order_items.keys():
            grouped_order_items[name]['quantity'] += order_item['quantity']
            grouped_order_items[name]['price'] += order_item['price']
        else:
            grouped_order_items[name] = order_item

    return grouped_order_items


def print_receipt(order_items):
    total = 0

    grouped_order_items = group_order_items(order_items)

    print('RECEIPT')
    for name, order_item in grouped_order_items.items():
        price = order_item['price']
        quantity = order_item['quantity']

        print(f"{name} - {quantity} - {price} pesos")

        total += price

    print(f"Total due: {total} pesos")


def get_order():
    order_items = []
    order_finished = False

    while not order_finished:
        order_item = get_order_item()
        order_items.append(order_item)

        add_order_item = ask_to_add_order_item()
        if add_order_item == False:
            order_finished = True

    print_receipt(order_items)


get_order()

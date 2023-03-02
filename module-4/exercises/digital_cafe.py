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
    while not (is_int(selected_product_id_string) and int(selected_product_id_string) in products.keys()):
        print('Invalid input')
        selected_product_id_string = input('Select a product: ')

    selected_product_id = int(selected_product_id_string)
    selected_product = products[selected_product_id]

    print(f"You have selected {selected_product['name']}")
    return selected_product


def get_quantity():
    quantity_string = input('Enter quantity: ')
    while not (is_int(quantity_string) and int(quantity_string) > 0):
        print('Invalid input')
        quantity_string = input('Enter quantity: ')

    quantity = int(quantity_string)
    return quantity


def get_order_item():
    selected_product = get_selected_product()
    quantity = get_quantity()

    order_item = selected_product.copy()
    order_item['quantity'] = quantity

    return order_item


def ask_to_add_order_item():
    pass


def print_receipt(order_items):
    pass


def get_order():
    order_items = []
    order_finished = False

    while not order_finished:
        order_item = get_order_item()
        order_items.append(order_item)

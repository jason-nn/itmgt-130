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


def get_selected_product_id():
    for id, product in products.items():
        print(f"Enter {id} for {product['name']}")

    selected_product_id_string = input('Select a product: ')
    while not (is_int(selected_product_id_string) and int(selected_product_id_string) in products.keys()):
        print('Invalid input')
        selected_product_id_string = input('Select a product: ')

    selected_product_id = int(selected_product_id_string)

    print(f"You have selected {products[selected_product_id]['name']}")
    return selected_product_id


def get_order_item():
    selected_product_id = get_selected_product_id()


get_order_item()

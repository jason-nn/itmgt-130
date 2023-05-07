products = {
    1: {
        'name': 'Tonkatsu',
        'price': 500
    },
    2: {
        'name': 'Curry',
        'price': 420
    },
    3: {
        'name': 'Katsudon',
        'price': 380
    }
}

accounts = {
    'jason': 'password',
    'john': 'doe'
}

order_statuses = {
    1: 'RECEIVED',
    2: 'PREPARING IN THE KITCHEN',
    3: 'PACKAGING',
    4: 'READY TO BE DELIVERED'
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
    grouped_order_items_raw = {}

    for order_item in order_items:
        name = order_item['name']
        if name in grouped_order_items_raw.keys():
            grouped_order_items_raw[name]['quantity'] += order_item['quantity']
            grouped_order_items_raw[name]['price'] += order_item['price']
        else:
            grouped_order_items_raw[name] = order_item

    grouped_order_items = grouped_order_items_raw.values()

    return grouped_order_items


def print_receipt(grouped_order_items):
    total = 0

    print('RECEIPT')
    for order_item in grouped_order_items:
        name = order_item['name']
        price = order_item['price']
        quantity = order_item['quantity']

        print(f"{name} - {quantity} - {price} pesos")

        total += price

    print(f"Total due: {total} pesos")
    print()


def get_order():
    order_items = []
    order_finished = False

    while not order_finished:
        order_item = get_order_item()
        order_items.append(order_item)

        add_order_item = ask_to_add_order_item()
        if add_order_item == False:
            order_finished = True

    grouped_order_items = group_order_items(order_items)

    print_receipt(grouped_order_items)

    return grouped_order_items


def get_total(grouped_order_items):
    total = 0

    for order_item in grouped_order_items:
        price = order_item['price']
        total += price

    return total


def ask_to_proceed_to_payment(total):
    print('Enter 1 for NO')
    print('Enter 2 for YES')

    user_input = input(f'Pay {total} pesos? ')
    print()
    while not (is_int(user_input) and int(user_input) in [1, 2]):
        print('Invalid input')
        user_input = input(f'Pay ${total} pesos? ')
        print()

    return bool(int(user_input)-1)


def validate_account_details(account_name, password):
    if account_name in accounts.keys():
        if password == accounts[account_name]:
            return True
        else:
            print('Password is incorrect.')
            return False
    else:
        print('Account does not exist.')
        return False


def process_payment(grouped_order_items):
    total = get_total(grouped_order_items)

    proceed_to_payment = ask_to_proceed_to_payment(total)

    if proceed_to_payment:
        account_name = input(f'Enter account name: ')
        password = input(f'Enter password: ')
        print()
        while not validate_account_details(account_name, password):
            print('Try entering account details again.')
            print()
            account_name = input(f'Enter account name: ')
            password = input(f'Enter password: ')
            print()

        print(f'Successfully processed payment of {total} pesos')
        print()
        return True
    else:
        print('Unsuccesful payment. Unfortunately, we will have to cancel your order.')
        print()
        return False


def show_order(grouped_order_items):
    print('ORDER DETAILS')
    for order_item in grouped_order_items:
        name = order_item['name']
        quantity = order_item['quantity']

        print(f"{name} - {quantity}")

    print()


def get_order_status(current_order_status):
    print(f'Order status is currently {order_statuses[current_order_status]}')

    for id, order_status in order_statuses.items():
        print(f"Enter {id} to change order status to {order_status}")

    selected_order_status = input('Select order status: ')
    print()
    while not (is_int(selected_order_status) and int(selected_order_status) in order_statuses.keys()):
        print('Invalid input')
        selected_order_status = input('Select order status: ')
        print()

    return int(selected_order_status)


def main():
    print('CUSTOMER FLOW')
    print('CUSTOMER FLOW')
    print('CUSTOMER FLOW')
    print()
    grouped_order_items = get_order()
    payment_successful = process_payment(grouped_order_items)

    if payment_successful:
        print('RESTAURANT FLOW')
        print('RESTAURANT FLOW')
        print('RESTAURANT FLOW')
        print()
        print('Order has been received.')
        print()
        show_order(grouped_order_items)

        order_status = 1

        while order_status != 4:
            new_order_status = get_order_status(order_status)
            order_status = new_order_status
            print(f'Order status is now {order_statuses[new_order_status]}')
            print()

        print('Order is now ready to be delivered.')
        print('Initiating call to Lalamove API to assign a driver.')


main()

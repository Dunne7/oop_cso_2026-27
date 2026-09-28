#A small shop stores its shopping basket as a list of dict

#Exercise C1 : Calculate the total of the basket

def total_basket(basket):
    total = 0

    for item in basket:

        price = item["price"]
        quantity = item["quantity"]
        total += (quantity * price)

    return total

if __name__ == "__main__":
    basket = [
        {"name": "Yogurt", "price": 1.79, "quantity": 4},
        {"name": "Bread", "price": 1.80, "quantity": 1},
        {"name": "Milk", "price": 1.59, "quantity": 2}
    ]


    print(total_basket(basket))

#Exercise C2 Display a formatted receipt

def print_receipt(basket):

    for item in basket:
        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]





"""
    Allows user to enter a product and quantity and then calculates the total price of the products. Will discount the total price based on the membership type.
"""

def getPrice(product, quanity):
    """
    Returns the subtotal of the product and quantity entered by the user.

    inputs:
        product: string
        quanity: int
    outputs:
        subtotal: int
    """
    priceData = {
        "Biscuits": 3,
        "Chicken": 5,
        "Egg": 1,
        "Fish": 3,
        "Coke": 2,
        "Bread": 1,
        "Apple": 3,
        "Onion": 3
    }
    subtotal = priceData.get(product) * int(quanity)
    print(f"{product} costs ${priceData[product]}")
    return subtotal


def enterProducts():
    """
    Returns a dictionary of the product and quantity entered by the user.
    """
    product = input("Enter name product: ").capitalize()
    quantity = int(input("Enter quantity: "))

    return {
        product: quantity,
    }


def getDiscount(billAmount, membership):
    """
    Returns the final bill amount after applying the discount based on the membership type.
    inputs:
        billAmount: int
        membership: string
    outputs:
        billAmount: int
    """
    if billAmount > 25:
        discount = 0
        if membership == "Gold":
            billAmount *= .8
            discount = 20
        elif membership == "Silver":
            billAmount *= .9
            discount = 10
        elif membership == "Bronze":
            billAmount *= .95
            discount = 5

        print(f"Discount: ${discount} for a final amount {billAmount}")
    else:
        print("No discount for less than 25")
    return billAmount


product_list = []
while True:
    choice = input("Press A to Enter New Products. Press Q to Quit: ").upper()
    if choice == "Q":
        break
    if choice != "A":
        print("Invalid choice")
        continue
    if choice == "A":
        product = enterProducts()
        product_list.append(product)

total = 0
for item in product_list:
    for product, quantity in item.items():
        total += getPrice(product, quantity)

print(f"Subtotal: ${total}")

member = input("Enter membership type: ").capitalize()
total = getDiscount(total, member)

print(f"Total: ${total}")

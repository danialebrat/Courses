
#  define the available products and their prices:
products = {"T-shirt": 20, "Hat": 10, "Mug": 5, "Jeans":15, "sweater": 25}


# Greet the user, ask their names
print("Welcome to our online store!")

# storing the name of the user
name = input("What is your name? ")

# printing some personalized message using their name
print(f"Hello {name} ! we have very great products to offer!")

# Show them the list of available products:

print("=" * 30)

for product, price in products.items():
    print(f"{product} : ${price}")

print("=" * 30)

# create an empty dictionary to store the user's order
# we can use this dictionary to store the name of the product they want to buy
# and the quantity of their order
# for example: they want to buy 3 Hat and 2 Mug
# the dictionary after adding their products will look like:
# order{"Hat": 3, "Mug": 2}


order = {}

# let them choose repeatedly
while True:

    # let them choose from the products and store their chosen product
    purchase = input("What do you like to buy (type 'done' when finished)?")

    # if they don't want to add more products, they can say "done", if they say
    # "done", we use "break" to get out of the while loop
    if purchase == "done":
        break

    # if their product is not one of our products, print a message and let them
    # choose again by using "continue"
    if purchase not in products:
        print("Sorry, that product is not available in our store!")
        continue

    # store the quantity of their chosen product
    quantity = input(f"How many {purchase} would you like to buy (enter a valid number)?")

    # add their product in the order dictionary, if they already have chosen that
    # before, incease the quantity by their new quantity
    if purchase in order:
        order[purchase] += int(quantity)

    # if they choose a new product, add it to the order dictionary
    else:
        order[purchase] = int(quantity)

# total price is zero at first, we will increase it using the chosen products
total_price = 0

# print their purchase, quantity and the total cost of that item
for purchase, quantity in order.items():
    price = products[purchase]
    cost = price * quantity
    total_price += cost
    print(f"{quantity} {purchase} added to your cart")

# get their information , address, phone:
address = input("what is your address?")
phone = input("what is your phone number?")

# print their recipt using their information, and the products:
print("=" * 30)
print("RECEIPT")
print("=" * 30)

print(f" Name: {name}")

# print the chosen products, the quantity and the price of each
for purchase, quantity in order.items():
    price = products[purchase]
    cost = price * quantity
    print(f" {quantity} {purchase} at ${price} each: ${cost}")

# print the total price
print(f" Total Price: {total_price}")
print(f" Address: {address}")
print(f" Phone number: {phone}")
print("=" * 30)


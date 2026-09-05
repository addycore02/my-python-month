#### SHOPPING CART ####

print(" SHOPPING CART ")

products = {
    "Guava": 20,
    "Spinach": 30,
    "Eggs": 70,
    "Milk": 100,
    "Chicken": 250,
    "Sprouts": 50
}

cart = []

while True:

    items = input(" Enter The Name Of Product You Want To Add : ").capitalize()

    if items in products:
        cart.append(items)

        price = products[items]

        print(f" {items} added to the cart")
        print(f" Price : ₹{price}")

    else:
        print(" Product Not Available")

    again = input(" Do you want to add another product? (yes/no) : ")

    if again.lower() == "no":
        break

print(f" Items in the cart are : {cart}")

total = 0

for item in cart:
    total = total + products[item]

print(f" Total Bill Amount  : ₹ {total} ")
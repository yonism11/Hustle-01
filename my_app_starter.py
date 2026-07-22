# ============================================================
# LAB 7  -  MY OWN ORDERING APP
# Week 7  -  Hack the Hood
# ============================================================
# Name: __________________
#
# This is YOUR app. YOU write the code.
# Do the tickets IN ORDER from the Lab 7 sheet.
# Run this file after EVERY ticket to check your work.
#
# My store sells: Sneakers and Slides
# ============================================================


# ============================================================
# DAY 1  -  BUILD YOUR ITEMS
# ============================================================

# TICKET 1: My item blueprint
#   A class for your item. Every item has a name and a price.
#   Write your class below.

class Sneaker:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # TICKET 3: The price guard
    #   Add a set_price method INSIDE your class above.
    #   It should say no to a price below zero.
    def set_price(self, amount):
        if amount < 0:
            print("Price cannot be negative!")
        else:
            self.price = amount


# TICKET 3: The price guard
#   Add a set_price method INSIDE your class above.
#   It should say no to a price below zero.
#   BREAK ON PURPOSE: after you build it, try item1.set_price(-5)
#   PREDICT what happens: It will print that the price cannot be negative.
#   Paste the message you see here: Price cannot be negative!



# TICKET 4: A second kind of item
#   A new class that copies (inherits from) your first class.
#   Write it below.

class Slide(Sneaker):
    pass



# TICKET 5: Each item's own action
#   Give each class its own method (deliver, serve, play...).
#   Same method name, different message.
#   EXPLAIN why the same name can do two things: 
#   Because each class can have its own version of the same method.

class Sneaker(Sneaker):
    def deliver(self):
        print("Shipping your sneakers!")


class Slide(Slide):
    def deliver(self):
        print("Sliding your order out the door!")



# TICKET 2: Make your real items
#   Make 2 or 3 real items with YOUR OWN names and prices.
#   PREDICT what print(item1.name) shows: It will show Adidas Adizero

item1 = Sneaker("Adidas Adizero", 130)
item2 = Sneaker("Nike Dunk Low", 120)
item3 = Slide("Adilette Slides", 35)

print(item1.name)



# ============================================================
# DAY 2  -  BUILD YOUR STORE
# ============================================================

# TICKET 6: My cart
#   A class that holds items in a list and can check out.
#   Write your Cart class below.

class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    # TICKET 9: Checkout  (add this method INSIDE your Cart class)
    #   Deliver every item and add up the total.

    def checkout(self):
        total = 0

        for item in self.items:
            item.deliver()
            total += item.price

        print("Total: $" + str(total))



# TICKET 7: My menu and my cart
#   A dictionary that gives each item a number, and one empty cart.

store = {
    "1": item1,
    "2": item2,
    "3": item3
}

cart = Cart()



# TICKET 8: Let customers shop
#   Use input() and a loop to keep adding picks until "done".
#   PREDICT what happens when you pick 1: 
#   It will add Adidas Adizero to the cart and print that it was added.

while True:
    choice = input("Pick 1, 2, 3, or 'done': ")

    if choice == "done":
        break

    elif choice in store:
        cart.add(store[choice])
        print(store[choice].name + " added!")

    else:
        print("That item does not exist.")



# TICKET 10: Test the whole app
#   Run it start to finish. PREDICT the full output first,
#   then check it against what really prints.

# PREDICT:
# If I choose 1 and 3 then type done:
# Adidas Adizero added!
# Adilette Slides added!
# Shipping your sneakers!
# Sliding your order out the door!
# Total: $165


cart.checkout()



# ============================================================
# CHALLENGE: add a THIRD kind of item, or your own feature!
# ============================================================
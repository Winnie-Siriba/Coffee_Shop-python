from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 5.0)
bob.create_order(latte, 6.0)
bob.create_order(latte, 3.0)
alice.create_order(espresso, 4.5)

print("Latte customers:", [c.name for c in latte.customers()])
print("Alice's coffees:", [c.name for c in alice.coffees()])
print("Average Latte price:", latte.average_price())
print("Most aficionado of Latte:", Customer.most_aficionado(latte).name)

from customer import Customer
from coffee import Coffee
from order import Order

benjamin = Customer("Benjamin")
esther = Customer("Esther")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

benjamin.create_order(latte, 5.0)
esther.create_order(latte, 6.0)
esther.create_order(latte, 3.0)
benjamin.create_order(espresso, 4.5)

print("Latte customers:", [c.name for c in latte.customers()])
print("Benjamin's coffees:", [c.name for c in benjamin.coffees()])
print("Average Latte price:", latte.average_price())
print("Most aficionado of Latte:", Customer.most_aficionado(latte).name)


import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_creation():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    with pytest.raises(Exception):
        Customer("")  

    with pytest.raises(Exception):
        Customer("A  long name over 15") 
    customer = Customer("John")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 4.5)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 4.5

def test_customer_orders_and_coffees():
    customer = Customer("Claire")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 6.0)

    assert len(customer.orders()) == 2
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()

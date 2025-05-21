import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_creation_valid():
    customer = Customer("Jules")
    coffee = Coffee("Flat White")
    order = Order(customer, coffee, 6.5)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 6.5

def test_order_invalid_price():
    customer = Customer("John")
    coffee = Coffee("Americano")

    with pytest.raises(Exception):
        Order(customer, coffee, 0.5)  # too low

    with pytest.raises(Exception):
        Order(customer, coffee, 11.0)  # too high

def test_order_invalid_types():
    coffee = Coffee("Latte")

    with pytest.raises(Exception):
        Order("NotACustomer", coffee, 5.0)

    customer = Customer("Emily")

    with pytest.raises(Exception):
        Order(customer, "NotACoffee", 5.0)

import pytest
from coffee import Coffee
from customer import Customer

def test_coffee_creation():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_name_validation():
    with pytest.raises(Exception):
        Coffee("A") 

def test_num_orders_and_average_price():
    coffee = Coffee("Mocha")
    customer1 = Customer("Winnie")
    customer2 = Customer("Jerry")

    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 7.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 6.0  

def test_customers_who_ordered_coffee():
    coffee = Coffee("Cappuccino")
    customer1 = Customer("Joan")
    customer2 = Customer("Lucy")

    customer1.create_order(coffee, 4.5)
    customer2.create_order(coffee, 6.0)

    customers = coffee.customers()
    assert customer1 in customers
    assert customer2 in customers

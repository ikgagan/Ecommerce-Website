import pytest
import random
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine
from IcecreamExceptions import ExceededRemainingChoicesException, OutOfStockException
from IcecreamExceptions import InvalidCombinationException
# Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm
    
@pytest.fixture
def first_order(machine):
    machine.reset()
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine
    
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("Waffle Cone")
    machine.handle_flavor("strawberry")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine

@pytest.fixture
def third_order(second_order, machine):
    machine.handle_container("Sugar Cone")
    machine.handle_flavor("chocolate")
    machine.handle_flavor("next")
    machine.handle_toppings("peanuts")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine

def test_first_selection(machine):
    try:
        # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
        # The order of the selection has to be correct. 
        # and it checks if the exception is raised if the order is not correct.
        machine.handle_flavor("vanilla")
        machine.handle_topping("peanuts")
        assert False
    except InvalidCombinationException:
        assert True

def test_flavours_instock(machine):
    try:
        # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
        # This test case checks if the exception is raised when the out of stock flavour is choosen by the user.
        machine.reset()
        tmp = machine.flavors[0].quantity
        machine.flavors[0].quantity=0
        machine.handle_container("cup")
        machine.handle_flavor(machine.flavors[0].name)
        assert False
    except OutOfStockException:
        machine.flavors[0].quantity=tmp
        assert True

def test_toppings_instock(machine):
    try:
        # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
        # This test case checks if the exception is raised when the out of stock toppings is choosen by the user.
        machine.reset()
        tmp = machine.toppings[0].quantity
        machine.toppings[0].quantity=0
        machine.handle_container("cup")
        machine.handle_flavor(machine.flavors[0].name)
        machine.handle_toppings(machine.toppings[0].name)
        assert False
    except OutOfStockException:
        machine.toppings[0].quantity = tmp
        assert True

def test_max_flavors(machine):
    try:
        # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
        # This test case checks if the exception is raised when the user chooses more the 3 flavours is choosen.
        machine.reset()
        machine.handle_container("cup")
        machine.handle_flavor(machine.flavors[0].name)
        machine.handle_flavor(machine.flavors[0].name)
        machine.handle_flavor(machine.flavors[0].name)
        machine.handle_flavor(machine.flavors[0].name)
        assert False
    except ExceededRemainingChoicesException:
        assert True

def test_max_toppings(machine):
    try:
        # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
        # This test case checks if the exception is raised when the user chooses more the 3 toppings is choosen.
        machine.handle_container("cup")
        machine.handle_toppings(machine.toppings[0].name)
        machine.handle_toppings(machine.toppings[0].name)
        machine.handle_toppings(machine.toppings[0].name)
        machine.handle_toppings(machine.toppings[0].name)
        assert False
    except ExceededRemainingChoicesException:
        assert True

def test_cost_calculation(machine):
    # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
    # This functions checks if the total cost returend by the calculate_cost is correct. 
    # it is checking for all scenarios like cup, toppings and flavour. 
    for i in range(4):
        expected_cost = 0
        machine.reset()
        random_container = random.choice(machine.containers)
        random_flavor = random.choice(machine.flavors)
        random_topping = random.choice(machine.toppings)
        expected_cost = random_container.cost + random_flavor.cost + random_topping.cost
        machine.handle_container(random_container.name)
        machine.handle_flavor(random_flavor.name)
        machine.handle_toppings(random_topping.name)
        if f"{expected_cost:.2f}" != f"{machine.calculate_cost():.2f}":
            assert False
        machine.handle_pay(machine.calculate_cost(), f"{expected_cost:.2f}")
    machine.reset()
    assert True 

def test_total_sales(third_order):
    # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
    # this functions test for total_sales 
    # if the total_sales is calculated properly
    # we are doing this test case using fixtures
    first_order_expected_cost = 2
    second_order_expected_cost = 2.5
    third_order_expected_cost = 2.25
    assert third_order.total_sales == first_order_expected_cost + second_order_expected_cost + third_order_expected_cost

def test_total_icecream(third_order):
    # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
    # this function is for total_icecream 
    # to check if the total_icecream  is increased properly
    # we are testing this function using fixtures 
    assert third_order.total_icecreams == 3
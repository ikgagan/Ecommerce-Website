import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import InvalidCombinationException, ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state
import random
# Gagan Indukala Krishna Murthy - gi36 - 3nd March 2023

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.reset()
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    # machine.handle_pay(10000,"10000")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("turkey")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("tomato")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    #machine.handle_pay(10000,"10000")
    return machine


@pytest.fixture
def third_order(second_order, machine):
    machine.handle_bun("no bun")
    machine.handle_patty("turkey")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    machine.handle_toppings("done")
    machine.handle_pay(machine.calculate_cost(), f"{machine.calculate_cost():.2f}")
    return machine

def test_first_selection(machine):
    try:
        # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
        # The order of the selection has to be correct. 
        # and it checks if the exception is raised if the order is not correct.
        machine.handle_patty("turkey")
        machine.handle_topping("cheese")
        assert False
    except InvalidCombinationException:
        assert True

def test_patty_instock(machine):
    try:
        # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
        # This test case checks if the exception is raised when the out of stock patty is choosen by the user.
        machine.reset()
        tmp = machine.patties[0].quantity
        machine.patties[0].quantity=0
        machine.handle_bun("no bun")
        machine.handle_patty(machine.patties[0].name)
        assert False
    except OutOfStockException:
        machine.patties[0].quantity=tmp
        assert True

def test_toppings_instock(machine):
    try:
        # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
        # This test case checks if the exception is raised when the out of stock toppings is choosen by the user.
        machine.reset()
        tmp = machine.toppings[0].quantity
        machine.toppings[0].quantity=0
        print(machine.currently_selecting)
        machine.handle_bun("White Burger Bun")
        machine.handle_patty(machine.patties[0].name)
        machine.handle_patty("next")
        machine.handle_toppings(machine.toppings[0].name)
        assert False
    except OutOfStockException:
        machine.toppings[0].quantity = tmp
        assert True

def test_max_patties(machine):
    try:
        # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
        # This test case checks if the exception is raised when the user chooses more the 3 patties is choosen.
        machine.reset()
        machine.handle_bun("no bun")
        machine.handle_patty(machine.patties[0].name)
        machine.handle_patty(machine.patties[0].name)
        machine.handle_patty(machine.patties[0].name)
        machine.handle_patty(machine.patties[0].name)
        assert False
    except ExceededRemainingChoicesException:
        assert True

# not working 
def test_max_toppings(machine):
    try:
        # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
        # This test case checks if the exception is raised when the user chooses more the 3 toppings is choosen.
        machine.handle_bun("White Burger Bun")
        machine.handle_patty("next")
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
    # it is checking for all scenarios like bun, patties and flavour using random module. 
    for i in range(4):
        expected_cost = 0
        machine.reset()
        random_buns = random.choice(machine.buns)
        random_patty = random.choice(machine.patties)
        random_topping = random.choice(machine.toppings)
        expected_cost = random_buns.cost + random_patty.cost + random_topping.cost
        machine.handle_bun(random_buns.name)
        machine.handle_patty(random_patty.name)
        machine.handle_patty("next")
        machine.handle_toppings(random_topping.name)
        machine.handle_toppings("done")
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
    first_order_expected_cost = 1
    second_order_expected_cost = 4
    third_order_expected_cost = 2.25
    assert third_order.total_sales == first_order_expected_cost + second_order_expected_cost + third_order_expected_cost

def test_total_burgers(third_order):
    # Gagan Indukala Krishna Murthy - gi36 - 2nd March 2023
    # this function is for total_icecream 
    # to check if the total_icecream  is increased properly
    # we are testing this function using fixtures 
    assert third_order.total_burgers == 3



# sample test case, can delete if not using
# def test_production_line(second_order):
#     for j in second_order.buns:
#         print(second_order.inprogress_burger)
#         if j.name.lower() == second_order.inprogress_burger[0].name.lower():
#             assert True
#             return

#     assert False

# add required test cases below
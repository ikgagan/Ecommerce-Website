# Gagan Indukala Krishna Murthy - gi36 - 27th feb 2023
from MyCalc import MyCalc # importing MyCalc class from MyCalc File 
import pytest # importing pytest framework which is used for software tests, including unit tests, integration tests, end-to-end tests, and functional tests.
calc = MyCalc() # assigning 
# Gagan Indukala Krishna Murthy - gi36 - 27th feb 2023

def test_many_add():
    # Gagan Indukala Krishna Murthy - gi36 - 27th feb 2023
    # testing using multiple values from this list
    data = [{
        "a":"2",
        "b":"2",
        "r":"4"
    },
    {
        "a":"4",
        "b":"4",
        "r":"8"
    },
    {
        "a":"1",
        "b":"1",
        "r":"2"
    },]
    for d in data:
        # Checking if the test cases match and pass with our add function by passing the list values to the add function
        # using assertion to debug the code
        assert calc.add(d["a"], d["b"]) == int(d["r"])

def test_many_sub():
    # Gagan Indukala Krishna Murthy - gi36 - 27th feb 2023
    # testing using multiple values from this list
    data = [{
        "a":"3",
        "b":"2",
        "r":"1"
    },
    {
        "a":"5",
        "b":"3",
        "r":"2"
    },
    {
        "a":"10",
        "b":"2",
        "r":"8"
    },]
    for d in data:
        # Checking if the test cases match and pass with our sub function by passing the list values to the sub function
        # using assertion to debug the code
        assert calc.sub(d["a"], d["b"]) == int(d["r"])

def test_many_mult():
    # Gagan Indukala Krishna Murthy - gi36 - 27th feb 2023
    # testing using multiple values from this list
    data = [{
        "a":"3",
        "b":"2",
        "r":"6"
    },
    {
        "a":"5",
        "b":"3",
        "r":"15"
    },
    {
        "a":"10",
        "b":"2",
        "r":"20"
    },]
    for d in data:
        # Checking if the test cases match and pass with our mult function by passing the list values to the mult function
        # using assertion to debug the code
        assert calc.mult(d["a"], d["b"]) == int(d["r"])

def test_many_div():
    # Gagan Indukala Krishna Murthy - gi36 - 27th feb 2023
    # testing using multiple values from this list
    data = [{
        "a":"10",
        "b":"2",
        "r":"5"
    },
    {
        "a":"9",
        "b":"3",
        "r":"3"
    },
    {
        "a":"15",
        "b":"3",
        "r":"5"
    },]
    for d in data:
        # Checking if the test cases match and pass with our div function by passing the list values to the div function
        # using assertion to debug the code
        assert calc.div(d["a"], d["b"]) == int(d["r"])


# Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
@pytest.fixture # using fixtures to hold the data so it's reusable
def my_calc_ans_add():
    calc.ans = "3" # keeping ans = 3 as the initial value
    return [{
        "a":"ans",
        "b":"2",
        "r":"5"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"4",
        "r":"9"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"1",
        "r":"10"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"1",
        "negative": True,
        "r":"1"
    },]

def test_data_ans_add(my_calc_ans_add):
    # Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
    for d in my_calc_ans_add:
        # using if condition to checking negative results 
        if "negative" in d and  d["negative"]:
            # giving wrong results as input value and checking if the test cases are passing
            assert calc.add(d["a"], d["b"]) != int(d["r"])
        else:
            # doing normal assertion like the above add test case.
            # passing a,b and the result 'r' to the add function and running the test case
            assert calc.add(d["a"], d["b"]) == int(d["r"])

# Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
@pytest.fixture # using fixtures to hold the data so it's reusable
def my_calc_ans_sub():
    calc.ans = "20" # keeping ans = 20 as the initial value
    # testing using multiple values from this list
    return [{
        "a":"ans",
        "b":"5",
        "r":"15"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"4",
        "r":"11"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"1",
        "r":"10"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"1",
        "negative": True,
        "r":"1"
    },]

def test_data_ans_sub(my_calc_ans_sub):
    # Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
    for d in my_calc_ans_sub:
        # using if condition to checking negative results 
        if "negative" in d and  d["negative"]:
            # giving wrong results as input value and checking if the test cases are passing
            assert calc.sub(d["a"], d["b"]) != int(d["r"])
        else:
            # doing normal assertion like the above sub test case.
            # passing a,b and the result 'r' to the sub function and running the test case
            assert calc.sub(d["a"], d["b"]) == int(d["r"])


# Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
@pytest.fixture # using fixtures to hold the data so it's reusable
def my_calc_ans_mult():
    calc.ans = "5" # keeping ans = 5 as the initial value
    return [{
        "a":"ans", 
        "b":"5",
        "r":"25"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"4",
        "r":"100"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"1",
        "r":"100"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"1",
        "negative": True,
        "r":"1"
    },]

def test_data_ans_mult(my_calc_ans_mult):
    # Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
    for d in my_calc_ans_mult:
        # using if condition to checking negative results 
        if "negative" in d and  d["negative"]:
            # giving wrong results as input value and checking if the test cases are passing
            assert calc.mult(d["a"], d["b"]) != int(d["r"])
        else:
            # doing normal assertion like the above mult test case.
            # passing a,b and the result 'r' to the mult function and running the test case
            assert calc.mult(d["a"], d["b"]) == int(d["r"])


# Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
@pytest.fixture # using fixtures to hold the data so it's reusable
def my_calc_ans_div():
    calc.ans = "20" # keeping ans = 20 as the initial value
    return [{
        "a":"ans",
        "b":"2",
        "r":"10"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"5",
        "r":"2"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"1",
        "r":"2"
    },
    {
        "a":"ans", # ans is getting updated and assigned to 'a' from the previous calculation 
        "b":"1",
        "negative": True,
        "r":"1"
    },]

def test_data_ans_div(my_calc_ans_div):
    # Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
    for d in my_calc_ans_div:
        # using if condition to checking negative results 
        if "negative" in d and  d["negative"]:
            # giving wrong results as input value and checking if the test cases are passing
            assert calc.div(d["a"], d["b"]) != int(d["r"])
        else:
            # doing normal assertion like the above div test case.
            # passing a,b and the result 'r' to the div function and running the test case
            assert calc.div(d["a"], d["b"]) == int(d["r"])
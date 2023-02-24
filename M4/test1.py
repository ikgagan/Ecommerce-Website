from MyCalc import MyCalc

# still working on the testing part 

import pytest
calc = MyCalc()

def test_many_add():
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
        assert calc.add(d["a"], d["b"]) == int(d["r"])

def test_many_sub():
    data = [{
        "a":"3",
        "b":"2",
        "r":"1"
    },
    {
        "a":"5",
        "b":"4",
        "r":"1"
    },
    {
        "a":"8",
        "b":"2",
        "r":"6"
    },]
    for d in data:
        assert calc.sub(d["a"], d["b"]) == int(d["r"])
        
def test_many_mult():
    data = [{
        "a":"3",
        "b":"2",
        "r":"6"
    },
    {
        "a":"5",
        "b":"4",
        "r":"20"
    },
    {
        "a":"8",
        "b":"2",
        "r":"16"
    },]
    for d in data:
        assert calc.mult(d["a"], d["b"]) == int(d["r"])

def test_many_div():
    data = [{
        "a":"6",
        "b":"2",
        "r":"3"
    },
    {
        "a":"10",
        "b":"2",
        "r":"5"
    },
    {
        "a":"9",
        "b":"3",
        "r":"3"
    },]
    for d in data:
        assert calc.div(d["a"], d["b"]) == int(d["r"])

@pytest.fixture
def my_calc_data():
    return [{
        "a":"6",
        "b":"2",
        "r":"8",
        "s":"4",
        "m":"12",
        "d":"3"
    },
    {
        "a":"10",
        "b":"2",
        "r":"12",
        "s":"8",
        "m":"20",
        "d":"5"
    },
    {
        "a":"15",
        "b":"3",
        "r":"18",
        "s":"12",
        "m":"45",
        "d":"5"
    }
    ]

def test_fix_data(my_calc_data):
    for d in my_calc_data:
        assert calc.add(d["a"],d["b"]) == int(d["r"])
        assert calc.sub(d["a"],d["b"]) == int(d["s"])
        assert calc.mult(d["a"],d["b"]) == int(d["m"])
        assert calc.div(d["a"],d["b"]) == int(d["d"])
    print(my_calc_data)
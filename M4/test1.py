# Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
from MyCalc import MyCalc # importing MyCalc class from MyCalc File 
import pytest # importing pytest framework which is used for software tests, including unit tests, integration tests, end-to-end tests, and functional tests.
calc = MyCalc() # assigning 
# Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
@pytest.fixture # using fixtures to hold the data so it's reusable

def my_calc_data():
    # Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
    # testing using multiple values from this dict
    data =  [{
        "a":"3",
        "b":"2",
        "add":"5",
        "sub":"1",
        "mult":"6",
        "div":"1.5",
        "2add":"7",
        "2sub":"-1",
        "2mult":"12",
        "2div":"0.75",
    },
    {
        "a":"4",
        "b":"4",
        "add":"8",
        "sub":"0",
        "mult":"16",
        "div":"1",
        "2add":"12",
        "2sub":"-4",
        "2mult":"64",
        "2div":"0.25",
    },
    {
        "a":"1",
        "b":"1",
        "add":"2",
        "sub":"0",
        "mult":"1",
        "div":"1",
        "2add":"3",
        "2sub":"-1",
        "2mult":"1",
        "2div":"1",
    },]
    return data

# Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023

def test_fix_data(my_calc_data):
    # Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
    for func,v in [(calc.add, 'add'), (calc.sub, 'sub'), (calc.mult, 'mult'), (calc.div, 'div')]:
        for d in my_calc_data:
            assert func(d["a"],d["b"]) == float(d[v])
            d[f"{v}_ans"] = func(d["a"],d["b"])

def test_result_calc(my_calc_data):
    # Gagan Indukala Krishna Murthy - gi36 - 26th feb 2023
    for func,v in [(calc.add, 'add'), (calc.sub, 'sub'), (calc.mult, 'mult'), (calc.div, 'div')]:
        for d in my_calc_data:
            assert func(d[f"{v}_ans"],d["b"]) == float(d[f"2{v}"])
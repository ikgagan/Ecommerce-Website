from MyCalc import MyCalc


def test_add():
    calc = MyCalc()
    check = calc.add(2, 2)
    assert check == 4

def test_sub():
    calc = MyCalc()
    check = calc.sub(3, 2)
    assert check == 1

def test_mult():
    calc = MyCalc()
    check = calc.mult(3, 2)
    assert check == 6
def add(a,b):
    print(f"\nAddition of {a} and {b} is {a+b}\n")

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
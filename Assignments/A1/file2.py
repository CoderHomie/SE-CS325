from file1 import math_func

@math_func
def add_floats():
    print("Provide 2 decimal numbers")
    num1 = input("Number 1")
    num2 = input("Number 2")
    return num1 + num2
# https://github.com/shaynasoroka-debug/lab11_SS_MC.git
# Partner 1: Shayna Soroka
# Partner 2: Maya Crecos

import math
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        quotient = b / a
        return quotient
    except ZeroDivisionError:
        print("ZeroDivisionError")
def logarithm(a, b):
    try:
        log = math.log(b,a)
    except ValueError:
        print("ValueError")
def exp(a, b):
    a ** b
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("ValueError")
def hypotenuse(a, b):
    return math.hypot(a, b)


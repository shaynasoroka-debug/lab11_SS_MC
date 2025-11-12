
import math
#hi

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b

def log(a, b):
    try:
        log = math.log(b,a)
    except ValueError:
        print("ValueError")
def exp(a, b):
    a ** b



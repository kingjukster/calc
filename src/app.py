import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

def log_value(x, base=math.e):
    if x <= 0:
        raise ValueError("log undefined for non positive values")
    if base <= 0 or base == 1:
        raise ValueError("invalid log base")
    return math.log(x, base)

def square(x):
    return x * x

def square_root(x):
    if x < 0:
        raise ValueError("square root of negative number")
    return math.sqrt(x)

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def percentage(base, percent):
    return base * percent / 100

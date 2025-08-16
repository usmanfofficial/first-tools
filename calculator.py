"""Tiny calculator utilities with a simple CLI."""

from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    return a + b

def sub(a: Number, b: Number) -> Number:
    return a - b

def mul(a: Number, b: Number) -> Number:
    return a * b

def div(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def pow_(a: Number, b: Number) -> Number:
    # exponentiation as a named function (avoid overriding built-in pow)
    return a ** b

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        print(add(float(sys.argv[1]), float(sys.argv[2])))
    else:
        print("Usage: python calculator.py 2 3")

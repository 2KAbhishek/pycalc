import math

class Calculator:
    def __init__(self, make, power_source):
        self.make = make
        self.power_source = power_source

    def __str__(self):
        """String representation of the calculator"""
        return f"Calculator by {self.make}, runs on {self.power_source}"

    def add(self, a, b):
        """Add two numbers together"""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers"""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b

    def divide(self, a, b):
        """Divide two numbers"""
        return a / b

    def exponent(self, a, b):
        """Raise a number to a power"""
        return a ** b

    def log(self, a, b):
        """Log a number to a base"""
        return math.log(a, b)

    def square_root(self, a):
        """Square root of a number"""
        return math.sqrt(a)

    def sin(self, a):
        """Sine of a number"""
        return math.sin(a)

    def cos(self, a):
        """Cosine of a number"""
        return math.cos(a)

    def tan(self, a):
        """Tangent of a number"""
        return math.tan(a)

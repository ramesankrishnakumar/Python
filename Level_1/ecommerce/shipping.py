from math import floor
from random import random


def calculate_shipping_cost():
    print(f"__name__={__name__}")
    return floor((random() * 100) + 1)

def calculate_sales_tax():
    print(f"__name__={__name__}")
    return floor((random() * 10) + 1)

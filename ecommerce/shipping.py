from math import floor
from random import random


def calculate_shipping_cost():
    return floor((random() * 100) + 1)

def calculate_sales_tax():
    return floor((random() * 10) + 1)

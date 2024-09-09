"""
Package is like a bigger container than a module
Below declaration will import everything form the shipping module
in ecommerce package
"""
import ecommerce.shipping

print(ecommerce.shipping.calculate_shipping_cost())

"""
Importing only the things we need
"""
from ecommerce.shipping import  calculate_shipping_cost, calculate_sales_tax

print(calculate_shipping_cost())
print(calculate_sales_tax())


"""
    for Importing the entire module
"""

from ecommerce import shipping

print(shipping.calculate_sales_tax())
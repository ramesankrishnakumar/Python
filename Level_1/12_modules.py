"""
 importing entire functions from the module
 This is like import java.util.*
"""
import converters
print(converters.kgs_to_lbs(85))

from converters import kgs_to_lbs

# here we don't have to prefix the functions with converters
print(kgs_to_lbs(85))


from utils import find_max

print(find_max([2, 200, 10, 1000, 20, 4, 56]))


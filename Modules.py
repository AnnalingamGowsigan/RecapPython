from Classes import TagCloud
from ecommerce.shopping import sales

import sys
print(sys.path)

sales.cal_tax()
# print(dir(sales))
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)

if __name__ == "__main":
    print("hiii")
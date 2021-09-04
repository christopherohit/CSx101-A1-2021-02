from decimal import *


a = float(input())
b = float(a * 0.0703069)
getcontext().prec = 6

print(Decimal(b).normalize())
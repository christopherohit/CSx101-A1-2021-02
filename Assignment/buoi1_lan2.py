#Transfer to C and K
from decimal import *




c = float(input())
Pc = ((c-32) * (5/9))
Pk = float(273.15 + Pc)

getcontext().prec = 6

print(Decimal(Pc).normalize() , round(Pk,3))

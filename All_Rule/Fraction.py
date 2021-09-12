from fractions import *

a , b = [int(x) for x in input().split()]

if b == 0:
    print("INVALID")
else:
    c = Fraction(a ,b)
    m = c.numerator
    n = c.denominator

    if (n == 1):
        print(m)
    else:
        print(m,n)

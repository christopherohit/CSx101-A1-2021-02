import math
from decimal import *

getcontext().prec = 4

def Tam_Giac(a ,b ,c):
    if c > b >= a:
        if (a**2 == b**2 + c**2):
            print("Tam giac vuong,","dien tich = {:.2f}".format(((1/2)*b*a)))
        elif( b == a):
            ha = (1/2)*c
            ha = float(ha)
            print("Tam giac can,","dien tich = {:.2f}".format((1/2)*b*ha))
        else:
            p = (a + b + c)/2
            ha = 2.((math.sqrt(p * (p - a) * (p - b) * (p - c)))/c)
            print("Tam giac thuong,","dien tich = {:.2f}".format((1/2)*(c*ha)))
    elif a + b == 2*c:
        print("Tam giac deu,","dien tich = {:.2f}".format(a**2.(math.sqrt(3)/4)))

a , b , c = [int(x) for x in input().split()]
Tam_Giac(a , b, c)

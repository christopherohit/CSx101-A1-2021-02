import math as m

a = int(input())
b = int(input())
c = int(input())

r = m.sqrt(abs(b))
q = a**5 - 2 * r + a * b * c

print(round(q,2))
import math as mp

a = int(input())
c = a * (mp.sqrt(2))

p = (a + a + c)/2
s = mp.sqrt(p*(p-a)*(p-a)*(p-c))
tongs = 4*s
finall_T = 2 * s
tr = pow(a,2) * mp.pi
semi_final = (tr - tongs)/2
bbb= semi_final + finall_T
print("{:.3f}".format(bbb))
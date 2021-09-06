'''
Nhập a, b, c là các số thực. In ra giá trị của biểu thức sau với 2 số lẻ sau dấu thập phân: 

x=a**5−2(√|b|)+a*b*c

INPUT
3 số thực a, b, c

OUTPUT
1 số với 2 số lẻ sau dấu thập phân
'''



a , b , c = list(map(float,input().split()))

r = float(abs(b)**(1/2))
q = a**5 - 2 * r + a * b * c
x = format(q,".2f")
print(x)
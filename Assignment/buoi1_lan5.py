
a , b , c = list(map(float,input().split()))

r = float(abs(b)**(1/2))
q = a**5 - 2 * r + a * b * c
x = format(q,".2f")
print(x)
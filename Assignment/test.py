
'''

t = int(input())
for i in range(t):
    n = int(input())
    print(n ** (1/3))
    print(type(n ** (1/3)))
    if type(n**(1/3)) is int:
        print("YES")
    else:
        print("NO")
'''

"""
n = int(input())
a= []
max = -1111111111111111111111111111111111
cou = 0
a[1:n] = [int(n) for n in input().split()]

for i in a:

    if cou <= 1:
        if (int(max) < int(i)):
            max = i
            cou += 1
if (max == -1111111111111111111111111111111111):
    print("NOT FOUND")

else:
    print(max)
    """

'''n = int(input())
a= []
a[0:n] = [n for n in input().split()]
b = sorted(a)
for i in range(len(b) -1 , -1 , -1):
    print(int(b[i]),end=" ")'''

"""n = int(input())
a = []
a[1:n] = [int(n) for n in input().split()]
count = 0
for i in a:
    if count < i:
        count = i
print(int(count))"""
'''
from math import sqrt

a ,b , c = [int(x) for x in input().split()]
p = (a + b + c)/2
p2 =int(a + b + c)
s = float(sqrt(p*(p-a)*(p-b)*(p-c)))
if a + b > c and a + c > b and b + c > a:
    print(int(p2),"{:.2f}".format(s))
else:
    print("NO")'''

# n = int(input())

# m = 'M'
# d = 'D'
# c = 'C'
# l = 'L'
# x = 'X'
# v = ''


# for i in range(n):
#     res = ""
#     a = input()
#     if (len(a)) == 4:
#         res = res + (a[0] * "M")




# n = int(input())
# arr = list(map(int, input().split()))
# arr = sorted(set(arr))
# print("{}".format("NOT FOUND" if len(arr) <= 1 else arr[-2]))

# t = int(input())
# while t > 0:
#     sp = 0
#     n = input()
#     if (len(n.split()) == 0):
#         print(0)
#     else:
#         for i in range(len(n)):
#             if (n[i] == " " and n[i+1] != " "):
#                 sp +=1
#         print(sp)
#     t -= 1



def Tinh(d):
    s = 1
    if d == 1:
        print("{:.8f}".format(d))
    else:
        for i in range(2, d):
            s = s + 1/i


n = int(input())
s = 1
a = 1
for a in range(n):
    d = int(input())
    for i in range(2,d+1):
        s+= 1/(a + i)
        a += i
    print("{:.8f}".format(s))

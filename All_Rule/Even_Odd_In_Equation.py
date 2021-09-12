
n = int(input())
s1 = 0 
s2 = 3*n + 1
if n == 0:
    print(0)
elif n % 2 == 0:
    for i in range(1 , s2):
        if (i % 2 == 0):
            s1 -= i
        else:
            s1 += i
    print(s1 + s2)
elif n % 2 != 0:
    for i in range(1, s2):
        if (i % 2 == 0):
            s1 -= i
        else:
            s1 += i
    print(s1 - s2)
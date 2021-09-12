def TTT(a,b):
    s = 0
    for i in range(a,0,-1):
        if a % i == 0:
            if b % i ==0:
                return i
                



a , b = [int(x) for x in input().split()]


if a == 2 or b == 2 or a == -2 or b == -2:
    print(2)
elif a == 1 or b == 1 or a == -1 or b == -1:
    print (1)
elif a == 0:
    print(b)
elif b == 0 :
    print(a)
else:
    a = abs(a)
    b = abs(b)
    if a < b:
        s =TTT(a,b)
        print(s)
    elif a >= b:
        s = TTT(b,a)
        print(s)
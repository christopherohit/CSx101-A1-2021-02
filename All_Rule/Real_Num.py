import math as mp

n = int(input())
if n <= 0 :
    print("NO")
else:
    a = mp.sqrt(n)

    if mp.sqrt(n) == round(a,1):
        print("YES")
    else:
        print("NO")
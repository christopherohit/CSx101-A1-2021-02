def YYY(n ,m):
    i = m
    while i > 0:
        if n % i == 0:
            if m % i == 0:
                print(i)
                break 
            else:
                i -= 1
        else:
            i -= 1
            if m % i == 0:
                if n % i == 0:
                    print(i)
                    break
    


m ,n = [int(x) for x in input().split()]
if n > m:
    YYY(n,m)
elif n == m :
    print(n)
else:
    YYY(m,n)

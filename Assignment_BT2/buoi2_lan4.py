import array





n = int(input())
x , y = [int(x) for x in input().split()]

#if n % 2 != 0:
if ( x  <= n // 2 + 2 and y <= (n//2)):
    print("White")
else:
    print("Black")

#else:
#    if x <= n / 2 + 1  
from decimal import Decimal, getcontext

# Print số lượng số có trong chuổi
getcontext().prec = 10^1000
n = int(input())
n = str(n)
a = len(n)
if int(n) < 0:
    a = len(n) - 1
    print(a)
else:
    print(a)
import math


def is_prime(n):
    count = 0
    for i in range (2 , int(math.sqrt(n))+1):
        if n % i == 0:
            count = count + 1
    if count == 0:
        return "YES"
    else:
        return "NO"


n = int(input())
if (n < 2):
    print("NO")
else:
    print(is_prime(n))



def checkPrimeNumber(n):
    if (n < 2):
        return False
    else:
        for i in range(2,n-1):
            if( n % i == 0):
                return False
            else:
                return True

n = 7
result = checkPrimeNumber(n)
print(result) 


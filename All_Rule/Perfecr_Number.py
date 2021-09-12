
n = int(input())
a = (n//2)+2
sum = 0

if n <= 1:
    print ("NO")
else:
    for i in range(1,a):
        if n % i == 0:
            sum += i

    if (sum == n):
        print("YES")
    else:
        print("NO")





def Tinh(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    else:
        return n * Tinh(n-1)



x , n = [int(x) for x in input().split()]
s = x
for i in range(2 , n + 1):
    s += (pow(x,n))/Tinh(n)
print("{:.2f}".format(s))
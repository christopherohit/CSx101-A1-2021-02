

#Tính Giai thừa với công thức (n!)/(k!*(n - k)!)
def Tinh(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    else:
        return n * Tinh(n-1)

n , k = [int(x) for x in input().split()]
a = n - k
q = Tinh(n)
w = Tinh(k)
e = Tinh(a)
c = q/(w*e)
print(int(c))

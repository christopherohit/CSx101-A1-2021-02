# m ,n = [int(x) for x in input().split(" ")]
m , n = list(map(int,input().split()))
c = 1000000007
kq = pow(m,n,c)
print(kq)

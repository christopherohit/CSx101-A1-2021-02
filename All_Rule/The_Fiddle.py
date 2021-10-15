n , k = [int(x) for x in input().split()]
a =[]
a[1:n] = [int(n) for n in input().split()]
t = 0
for i in a:
    t += i
left = t
for i in a:
    if left > k:
        left = left - min(a)
    else:
        print(left)
        break
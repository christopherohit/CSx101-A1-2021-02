

def swap(s1, s2):
    return s2, s1

def Process():
    if (k == 1):
        return 0
    if n < k:
        if m == k: return k - 1
        if y == 1 or y == m:
            return k - 1
        else: return k

    if (x == 1 or x == n) and (y == 1 or y == m): return k
    if x == 1 or x == n or y == 1 or y == m:
        if y == 1 or y == m:
            swap(n ,m),swap(x,y)
        return k + (y >= k and (m - y + 1 >= k))

    drx0 = n > k
    drx1 = n >= k
    dxl = (n-x+1) >= k
    dxr = x >= k
    dry0 = m > k
    dry1 = m >= k
    dyl = (m-y+1) >= k
    dyr = y >= k
    return k - 1 + min(drx0 + dry1 + dyl*dyr, dry0+drx1+dxl*dxr)


n , m = [int(j) for j in input().split()]
x, y = [int(j) for j in input().split()]
k = int(input())
if (n > m):
    swap(n ,m)
    swap(x ,y)
res = Process()
print(res)

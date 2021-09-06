def s(n):
    if n == 1:
        return n
    else:
        return n * s(n - 1)

n = int(input())
print(s(n))    
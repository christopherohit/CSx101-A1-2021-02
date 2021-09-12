n = int(input())
a= []
max = -1111111111111111111111111111111111
a[1:n] = [n for n in input().split()]

for i in a:
    if (int(max) < int(i)):
        max = i

print(max)
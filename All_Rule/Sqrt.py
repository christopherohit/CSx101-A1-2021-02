n = int(input())
a = []
a[1:n] = [int(n) for n in input().split()]
count = -100000000000000000000000000000000000000000000000
poi = 0
for i in range(len(a)):
    if count < a[i]:
        count = a[i]
        poi = i
    elif count == a[i]:
        poi = i
print(int(poi))
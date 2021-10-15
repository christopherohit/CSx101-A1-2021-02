m , n = [int(x) for x in input().split()]

count = 0

for i in range(n-1 , m,-1):
    if (i % 3 == 0):
        print(i,end=" ")
        count += 1

if count == 0:
	print("NOT FOUND")
    
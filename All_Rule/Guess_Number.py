import random
n = random.randint(0,10)
k = 0

while k < 2:
    i = int(input())
    if i == n:
        print("GOOD")
        k += 1
        break
    else:
        if i > n:
            print("HIGH")
            k +=1
            continue
        else:
            print("LOWER")
            k += 1
            continue
if k > 2:
    print(n)
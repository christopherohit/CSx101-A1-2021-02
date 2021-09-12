


n = int(input())
s = 1
a = 1
i = 2
for a in range(n):
    d = int(input())
    while i <= d:
        a +=i
        s+= 1/(a)
        
        
    print("{:.8f}".format(s))

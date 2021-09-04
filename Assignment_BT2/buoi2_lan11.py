n = int(input())

def Rut_Gon(a , b):
    k = 1
    if a>b :
        for i in range(2, b+1):
            if a%i == 0 and b % i == 0:
                k = i
        t = a/k
        m = b/k
        if(m > 1):
            print(int(t),int(m))
        else:
            print(int(t))
    else:
        for i in range(2, a+1):
            if a%i == 0 and b % i == 0:
                k = i
        t = a/k
        m = b/k
        if(m > 1):        
            print(int(t),int(m))    
        else:
            print(int(t))

for i in range(n):
    x , y = [int(x) for x in input().split()]
    Rut_Gon(x ,y)
 
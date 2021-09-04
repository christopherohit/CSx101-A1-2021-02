n = int(input())

def Rut_Gon(x , y):
    if y == 1:
        return 0
    elif x > y:
        for i in range(2 , y+1):
            if (x % i == 0 and y % i ==0):
                print(p = x//i)
                print(q = y//i)
    elif x <= 0:
        return "Error"
    elif x < y:
        for i in range(2 , x + 1):
            if x % i == 0 & y % i == 0:
                print(x//i)
                print(y//i)


for i in range(n):
    x , y = [int(x) for x in input().split()]
    Rut_Gon(x,y)

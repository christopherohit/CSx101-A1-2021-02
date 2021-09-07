'''
Viết chương trình rút gọn phân số.

INPUT

Dòng đầu tiên là một số nguyên 
n(1≤n≤100) — Số lượng phân số cần rút gọn

n dòng tiếp theo là hai số nguyên a,b(a,b≥1)— a,b lần lượt là tử số và mẫu số.

OUTPUT

Ứng với n dòng, in ra theo thứ tự tử số và mẫu số (cách nhau một khoảng trắng) 
sau khi rút gọn; mẫu số chỉ được in khi lớn hơn 1.
'''


from fractions import *

n = int(input())

def Rut_Gon(a , b):
    '''k = 1
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
'''
    c = Fraction(x,y)
    a = c.numerator
    b = c.denominator
    if( b == 1):
        print(a)
    else:
        print(a,b)


for i in range(n):
    x , y = [int(x) for x in input().split()]
    Rut_Gon(x ,y)

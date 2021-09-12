'''
#Trans to Binary - Manual
def Trans_To_Bin(a):
    s = ''
    w = ''
    while a >= 1:
        k = a % 2
        a = int(a/2)
        s += str(k)
    for i in range(len(s),0,-1 ):
        w += s[i-1]
    return w
n = int(input())
for i in range(n):
    a = int(input())
    if (a == 0):
        print(0)
    else:
        v = Trans_To_Bin(a)
        print(int(v))'''

# By library

n = int(input())
for i in range(n):
    a = int(input())
    print("{0:b}".format(a))
import math as mp
def giaiPTBac2(a, b, c):
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            print ("NO")
        else:
            print ("{:.2f}".format(-c / b))
        return;
 
    # tính delta
    delta = b * b - 4 * a * c
    # tính nghiệm
    if (delta > 0):
        x1 = (float)((-b + mp.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - mp.sqrt(delta)) / (2 * a))
        print ("{:.2f}".format(x2), "{:.2f}".format(x1))
    elif (delta == 0):
        x1 = (-b / (2 * a))
        print("{:.2f}".format(x1))
    else:
        print("NO");import math




a ,b ,c = [int(x) for x in input().split()]
giaiPTBac2(a, b, c)
Tr, Xd, Cr, Rk = [int(x) for x in input().split()]

if (Tr == 1):
    if(Xd == 1 or Rk == 1):
        if (Cr == 1):
            print(1)
        else:
            print(0)
    elif Xd == 0:
        print(0)
    elif Rk == 1 or Rk == 0:
        print(1)
else:
    if (Xd == 1):
        print(0)
    elif Rk == 1:
        if Cr == 1:
            print(1)
        else:
            print(1)
    elif Xd == 0 and Rk == 1:
        if Cr == 1:
            print(1)
        else:
            print(0)
    elif Xd == 0 and Rk == 0:
        if Cr == 1 :
            print(0)
        else:
            print(1)
    else:
        print(1)

a , b  , c ,d ,e ,f = [int(x) for x in input().split()]

if a/d == b/e and b/e != c/f:
    print("VONGHIEM")
elif a/d == b/e and b/e == c/f:
    print("VOSONGHIEM")
else:
    y = (c*d - a*f)/(b*d - e)
    x = (f- e*y)/d
    print("{:.2f}".format(x),"{:.2f}".format(y))
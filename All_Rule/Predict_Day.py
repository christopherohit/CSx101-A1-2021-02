def checkYear(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    else:
        return False

def Day(a, t):
    dict={
        1:31,
        2:int(a),
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }
    return dict.get(t)

    

t , y = [int(x) for x in input().split()]
a = 28
if t > 12 or t < 1 or y == 0:
    print("INVALID")
else:
    if checkYear(y) is True:
        a = 29
        print(Day(a,t))
    else:
        print(Day(a,t))
    
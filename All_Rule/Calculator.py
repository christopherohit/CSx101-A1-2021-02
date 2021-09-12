a, c ,b = [str(x) for x in input().split()]
a = float(a)
b = float(b)

if (b == 0):
    print("Math Error")
else:
    sign = {
    '+' : a + b,
    '-' : a - b,
    '*' : a * b,
    '/' : a / b,
    }

    r = sign.get(c,"")
    print("{:.2f}".format(float(r)))


'''
Nhận dạng tam giác

Viết chương trình nhập vào 3 số thực. Hãy cho biết đó có phải là độ dài 3 cạnh 1 tam giác hay không? Nếu phải thì đó là loại nào trong 4 loại sau: tam giác thường, cân, đều, vuông.

Nếu là tam giác tính diện tích tam giác.

INPUT:

Dòng đầu tiên là độ dài cạnh 1.

Dòng thứ hai là độ dài cạnh 2.

Dòng thứ ba là độ dài cạnh 3.

OUTPUT

Định dạng như ví dụ minh họa. Diện tích làm tròn 02 chữ số sau dấu thập phân.
'''


import math
a , b , c = [int(x) for x in input().split()]
if a + b > c and a + c > b and b + c > a:
    if a == b or b == c or c == a:
        ha = float((1/2)*c)
        dt = float((1/2)*b*ha)
        print("Tam giac can,","dien tich = {:.1f}".format(dt))
    if c*c == b*b + a*a :
        dt = float((1/2)*b*a)
        print("Tam giac vuong,","dien tich =",round(dt,1))
    elif a == b and b == c:
        dt = float(a**2 * ((math.sqrt(3))/4))
        print("Tam giac deu,","dien tich = {:.1f}".format(dt))
    else:
        p = float((a + b + c)/2)
        ha = float(2*((math.sqrt(p * (p - c) * (p - b) * (p - a)))/c))
        dt = float((1/2)*c*ha)
        print("Tam giac thuong,","dien tich = {:.1f}".format(dt))
else:
    print("Khong phai tam giac")

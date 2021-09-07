'''
Nhận dạng tam giác

Viết chương trình nhập vào 3 số thực. Hãy cho biết đó có phải là độ dài 3 cạnh 1 tam giác hay không? 
Nếu phải thì đó là loại nào trong 4 loại sau: tam giác thường, cân, đều, vuông.
Nếu là tam giác tính diện tích tam giác.
INPUT:

Dòng đầu tiên là độ dài cạnh 1.

Dòng thứ hai là độ dài cạnh 2.

Dòng thứ ba là độ dài cạnh 3.

OUTPUT

Định dạng như ví dụ minh họa. Diện tích làm tròn 02 chữ số sau dấu thập phân.
'''


import math

a = float(input())
b = float(input())
c = float(input())

p = (a + b + c)/2
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
if s == int(s):
    s = int(s)
else:
    s = round(s,2)
if a + b > c and a + c > b and b + c > a:
    if ((a == b  and a!= c) or (a == c and a!=b) or (b == c and b != a)):
        print("Tam giac can,","dien tich =",s)
    elif c*c == b*b + a*a or a*a == b*b + c*c  or b*b == a*a + c*c:
        print("Tam giac vuong,","dien tich =",s)
    elif a == b and b == c:
        print("Tam giac deu,","dien tich =",s)
    else:
        print("Tam giac thuong,","dien tich =",s)
else:
    print("Khong phai tam giac")

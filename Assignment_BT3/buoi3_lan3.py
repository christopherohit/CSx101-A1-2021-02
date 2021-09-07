'''
Nhập vào số nguyên x sao cho 1 ≤ x ≤ 30. Nếu x không thỏa điều kiện,
chương trình xuất ra màn hình thông báo “So <x> khong nam trong khoang [1,30].”. 
Nếu x nằm trong đoạn [1,30], chương trình xuất ra màn hình số Fibonacci thứ x.
'''



n = int(input())

def Fibp(n):
    if n <= 2:
        return 1
    elif n < 0:
        return -1
    else:
        return Fibp(n -1) + Fibp(n - 2)

if (1 <= n <= 30):
    print(Fibp(n))
else:
    print("So",n,"khong nam trong khoang [1,30].")


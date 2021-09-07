'''
Viết chương trình tính tổng các ước số thực sự của một số nguyên dương.

INPUT

Số nguyên dương n giá trị không quá 1 tỷ.

OUTPUT

Tổng các ước số của n (không kể n)
'''



n = int(input())
count = 0
for i in range(1,n):
    if (n % i == 0):
        count += i
print(count)
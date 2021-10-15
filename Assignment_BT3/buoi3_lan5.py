'''
Bình có một ma trận 5x5, bao gồm 24 số không và 1 số một với thứ tự ngẫu nhiên. 
Chỉ số các hàng và cột của ma trận được đánh số lần lượt từ 1 đến 5.
Bình là một người rất kĩ tính và chỉ thích những thứ gì cân bằng và đồng đều.
Chính vì vậy, anh ấy chỉ thích các ma trận mà có vị trí số một nằm ở giữa. 
Các bước hợp lệ để thay đổi một ma trận bao gồm: hoán vị hai hàng liền kề của ma trận và
hoán vị hai cột liền kề của ma trận.
Hãy giúp Bình tìm số bước hợp lệ tối thiểu để biến một ma trận thỏa mãn sở thích của anh ấy.

INPUT
Một ma trận 5x5 chứa 24 số không và 1 số một.

OUTPUT
Số bước hợp lệ tối thiểu để biến đổi ma trận.
'''

#Auto print Matrix
'''
a = []
auto = 0
for i in range(5):
    if auto == 0:
        n = int(input())
        if n == 1:
            a.append([n])
            auto += 1
            for j in range(4):
                k = int(input())
                a[i].append(0)
        else:
            a.append([n])
            for j in range(4):
                if auto == 1:
                    a[i].append(0)
                else:
                    k = int(input())
                    if k == 1:
                        auto += 1
                    a[i].append(k)
                
    elif auto == 1:
        a.append([0])
        for j in range(5):
            a[i].append(0)

print(a)
'''
# Uncompleted

x = 1
y = 1

a = []
for i in range(5):
    n = int(input())
    if(n == 1):
        a.append([n])
        if i == 0:
            x = 1
            y = 1
        else:
            x = i
    else:
        a.append([n])
    for j in range(4):
        k = int(input())
        if (k == 1):
            a[i].append(k)
            y += 1
            y = y
        else:
            a[i].append(k)
            y += 1
sumx , sumy = 0 , 0

while x < 3:
    sumx += 1
    x += 1
while x > 3:
    sumx += 1
    x -= 1
while y > 3:
    sumy += 1
    y -= 1
while y < 3:
    sumy += 1
    y += 1

tong_buoc_di = sumx + sumy
print(tong_buoc_di)

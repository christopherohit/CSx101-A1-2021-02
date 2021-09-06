# Gà Chó
'''
Gà và Chó

Vừa gà vừa chó

Bó lại cho tròn

xxx con

yy chân chẵn

Hãy xác định số con gà và số con chó thỏa mãn yêu cầu.

Dữ liệu: Vào từ thiết bị nhập chuẩn gồm 1 dòng ghi 2 số nguyên xxx và yy (2≤ xxx, yy ≤ 109)

Kết quả: Đưa ra thiết bị xuất chuẩn một dòng 2 số nguyên số gà và số chó tìm được.

Dữ liệu luôn bảo đảm có kết quả.
'''




n , c = list(map(int,input().split()))

y = (c - 4*n)/-2

x = n - y

print(int(y),int(x))

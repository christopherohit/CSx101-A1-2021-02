'''
Hầu hét các giải bóng đá lớn bắt đầu bằng vòng bảng, mỗi bảng 4 đội. Trong vòng này mỗi đội sẽ 
đá vòng tròn trong bảng mình như vậy tổng cộng là 03 trận. Sau đó 02 đôi có thành tích tốt nhất 
ở mỗi bảng sẽ vào vòng trong.

Ngoài ra có một số giải đấu người ta còn xét vé vớt vào vòng trong cho các đội xếp hạng 03 ở các bảng 
(như giải Asian Cup đang diễn ra). 
Để xếp thứ hạng cho các đội này người ta dựa vào 03 chỉ số thành tích theo thứ tự ưu tiên là:

Điểm số đạt được (Points). Trận thắng được 03 điểm, trận hòa được 1 điểm, thua 0 có điểm.
Hiệu số bàn thắng (Goal difference = Goal for - Goal against)
Số bàn thắng ghi được (Goal For)
Chỉ số fair play, thể hiện qua số thẻ vàng (yellow card) mà đội nhận (càng ít càng tốt)
Cho kết quả các trận đấu cả 02 đội. Tính xem đội nào có thành tích tốt hơn.

INPUT
Input gồm 6 hàng trong đó kết quả của một đội là 03 hàng, mỗi hàng có 03 con số nguyên lần lượt là:

Số bàn thắng (goal for)
Số bàn thua (goal against)
Số thẻ vàng (yellow card)
OUTPUT
Thành tích của đội tốt nhất  gồm 04 số nguyên lần lượt là:

Điểm số
Hiệu số bàn thắng
Số bàn thắng
Chỉ số fair play.
'''



ds, hs , bt , fp = 0, 0 , 0 , 0
ds1, hs1, bt1, fp1 = 0 , 0 , 0 , 0

for i in range(6):
    a , b , c = [int(x) for x in input().split()]
    if (i <3):
        if (a > b):
            ds += 3
        elif a == b:
            ds += 1
        hs += (a - b)
        bt += a
        fp += c
    else:
        if (a > b):
            ds1 += 3
        elif a == b:
            ds1 += 1
        hs1 += (a - b)
        bt1 += a
        fp1 += c



if (ds > ds1):
    print(ds , hs , bt, fp)
elif ds1 > ds:
    print(ds1, hs1,bt1 ,fp1)
else:
    if(hs > hs1):
        print(ds , hs , bt, fp)
    elif hs1 > hs:
        print(ds1, hs1,bt1 ,fp1)
    else:
        if(bt > bt1):
            print(ds , hs , bt, fp)
        elif bt1 > bt:
            print(ds1, hs1,bt1 ,fp1)
        else:
            if fp < fp1:
                print(ds , hs , bt, fp)
            elif fp1 < fp:
                print(ds1, hs1,bt1 ,fp1)


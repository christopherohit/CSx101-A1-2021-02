'''
Sau khi quan sát nhân tình thế thái, Bình rút ra 3 chân lý.

1. "Mấy đứa trẻ trung đều đẹp cả"

2. "Mấy đứa đẹp đều có người yêu"

3. "Mấy đứa không đẹp mà cũng có người yêu chắc chắn là vì nó giàu"

Cho 4 biến logic tre_trung, xinh_dep, co_gau, giau_co. Tương ứng với giá trị của các mệnh đề

1. Bạn X trẻ trung

2. Bạn X xinh đẹp

3. Bạn X có người yêu

4. Bạn X giàu có

Viết chương trình kiểm tra xem X có thoã các chân lý mà Bình quan sát được không

INPUT
4 biến logic như mô tả

OUTPUT
Giá trị 0 nếu 4 biến trên không thoã mãn các chân lý của Bình

Giá trị 1 nếu 4 biến trên thoã mãn
'''


Tr, Xd, Cr, Rk = [int(x) for x in input().split()]

if (Tr == 1):
    if(Xd == 1 or Rk == 1):
        if (Cr == 1):
            print(1)
        else:
            print(0)
    elif Xd == 0:
        print(0)
    elif Rk == 1 or Rk == 0:
        print(1)
else:
    if (Xd == 1):
        print(0)
    elif Rk == 1:
        if Cr == 1:
            print(1)
        else:
            print(1)
    elif Xd == 0 and Rk == 1:
        if Cr == 1:
            print(1)
        else:
            print(0)
    elif Xd == 0 and Rk == 0:
        if Cr == 1 :
            print(0)
        else:
            print(1)
    else:
        print(1)

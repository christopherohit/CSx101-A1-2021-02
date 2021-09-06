'''
Alice và Bob là đôi bạn thân trong lớp và thường giúp nhau trong giờ học. Hôm nay sẽ có tiết kiểm tra toán và như mọi khi – sẽ có k đề khác nhau. Lớp học có n học sinh. Các bàn trong lớp xếp thành một hàng dọc, mỗi bàn 2 người ngồi. Vị trí bên trái của bàn đánh số là 1, vị trí bên phải – đánh số 2. Đề bài được phát bắt đầu từ vị trí 1 của bàn 1 rồi đến vị trí 2 của bàn 1, tiếp theo là vị trí 1 của bàn 2, rồi tới vị trí 2 của bàn 2, . . . lần lượt các đề 1, đề 2, đề 3, . . . cho tới đề k rồi lại quay lại đề 1, đề 2, . . . cho tới khi tất cả các học sinh đều nhận được đề.

Alice đến trước và ngồi vào vị trí quen thuộc của mình: hàng p và vị trí q. Bob đến sau và muốn ngồi vào nơi sẽ nhận được cùng đề với Alice và ở dãy bàn gần với dãy bàn của Alice nhất. Nếu có 2 cách ngồi thì Bob sẽ chọn bàn ở phía trước của Alice.

Hãy xác định bàn u và vị trí v trong bàn nơi Bob cần phải ngồi. Nếu không có cách ngồi thỏa mãn thì đưa ra một số -1.

Dữ liệu: Vào từ thiết bị nhập chuẩn:

Dòng đầu tiên chứa một số nguyên n (2 ≤ n ≤ 109),
Dòng thứ 2 chứa số nguyên k (2 ≤ k ≤ n),
Dòng thứ 3 chứa số nguyên p (1 ≤ p ≤ (n+1)/2),
Dòng thứ 4 chứa số nguyên q (1 ≤ q ≤ 2).
Kết quả: Đưa ra thiết bị xuất chuẩn một dòng 2 số nguyên u và v tìm được hoặc số -1 nếu không có cách ngồi thỏa mãn điều kiện đã nêu.

Ví dụ:

INPUT           OUTPUT

25

2               2 2

1

2



'''



def Tinhtoan(n , k):
    for i in k:
        pass

n = int(input())
while(True):
    k = int(input())
    p = int(input())
    q = int(input())
    if(k < 2 or k > n or p < 1 or p > (n + 1)/2 or q < 1 or q > 2):
        if (k == n + 1):
            print("No Solution Because This Test Have "+ k + " topic for "+ n + " student" )
            continue
        elif (k < 2 ):
            print("Math Error it have many solution for This question");
            continue
        else:
            print("Error or Wrong something which is incorrect to condition of Threads");
            
    else:
        pass
        



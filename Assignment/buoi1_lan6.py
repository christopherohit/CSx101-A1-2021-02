'''
Để trang trí phòng phục vụ tổ chức sinh nhật cho một người bạn Alice lấy một tờ giấy màu thủ công 
kẻ ô vuông kích thước n×m (n hàng và m cột), cắt thành hình lò xo xoắn theo hướng phải sang trái và 
có độ rộng của đường bằng 1:

Bắt đầu từ biên phải cột 0 cắt lên trên cho đến khi cách lề trên một ô,
Cắt sang phải theo đường biên dưới cho đến khi cách lề phải một ô,
Cắt xuống dưới, rồi sang trái, sau đó lên trên,  . . . để có băng giấy độ rộng 1 ô,
Quá trình cắt sẽ dừng khi không cách cắt tiếp mà không làm đứt băng giấy.
Hãy tính tổng độ dài đường cắt theo đơn vị ô.

Dữ liệu: Vào từ thiết bị nhập chuẩn gồm một dòng chứa 2 số nguyên n và m (2 ≤ n, m ≤ 109).

Kết quả: Đưa ra thiết bị xuất chuẩn một số nguyên – độ dài đường cắt.

'''




#Version cuc suc

n , m = [int(x) for x in input().split()]
m = m -1
kq = 0
a = ((n*(n -1 ))/2)
p = ((m*(m - 1))/2)

print(int(a + p))

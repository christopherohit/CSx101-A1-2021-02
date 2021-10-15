'''
Jim thích các phim và truyện kết thúc có hậu. Một lần gặp may với số n và từ đó Jim rất có cảm tình với tất cả các số nguyên kết thúc bằng n, 
coi chúng là những số có hậu. Ví dụ với n = 25 thì các số 625, 553325,1025 là những số có hậu, còn 3255 – không có hậu!

Jim không thích các ràng buộc và hạn chế. Nhưng trong thế giới thực của chúng ta ràng buộc và hạn chế là điều tất yếu. Một người bạn của Jim 
khuyên chỉ nên quan tâm đến các số nguyên không vượt quá m và dĩ nhiên, Jim muốn biết có bao nhiêu số có hậu không vượt quá m.

Dữ liệu: Vào từ thiết bị nhập chuẩn gồm một dòng chứa 2 số nguyên n và m (1 ≤ n ≤ m ≤ 2×109).

Kết quả: Đưa ra thiết bị xuất chuẩn một số nguyên – số lượng số có hậu tìm được.

Ví dụ:

INPUT       OUTPUT
23 122        1

'''

# n ,m = input().split()
# a = len(str(n))
# before = m[0:len(m) - len(n)]

# after = m[len(before):]
# if (len(m) == len(n) == 1 or len(before) == ''):
#     print("1")
# else:
#     print(int(before) + int(int(after) >= int(n)))



'''

'''
n , m = input().split()
count = 0
if int(n) and int(m) <= 10:
    if n == m:
        print(1)
else:
    for i in m:
        if int(i) >= 100:
            pass
        else:
            a = int(i[-2] + i[-1])
            if a == n:
                count += 1
print(count)

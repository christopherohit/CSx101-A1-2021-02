'''
An và Bình rất thích ăn dưa hấu vì thế họ đi ra chợ chọn mua một trái to và chín nhất.  
Về đến nhà, một vấn đề nảy sinh đó là việc chia phần trái dưa hấu cho cả 2,
không chỉ thế, do 2 người bạn chỉ thích những con số chẵn, vì thế cần chia quả dưa hấu 
làm sao cho mỗi phần có khối lượng là một con số chẵn. 
Hãy giúp An và Bình kiểm tra xem có thể chia quả dưa hấu này hay không.

INPUT
Một số nguyên không âm

OUTPUT
Xuất YES nếu có thể chia, ngược lại NO
'''


a = int(input())

if (a % 2 == 0 and a > 2 ):
    print("YES")
else:
    print("NO")
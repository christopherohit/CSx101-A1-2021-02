'''
Số may mắn là các số nguyên dương chỉ chứa các chữ số là 4 hoặc 7.

Bình thích sự may mắn, tuy nhiên số lượng số may mắn không nhiều. Chính vì thế, 
Bình định nghĩa ra một loại số mới, gọi là số gần may mắn với điều kiện số chữ số may mắn 
trong số đó là một số may mắn.

INPUT
Một số nguyên dương n (n <= 1018).

OUTPUT
In ra YES nếu số đó là một số gần may mắn, ngược lại in NO.


'''



n = int(input())
k = str(n)
cout = 0
for i in k:
    if int(i) == 7 and int(i) == 4:    
        cout += 1
if (cout >=1 ):
    print("YES")
else:
    print("NO")
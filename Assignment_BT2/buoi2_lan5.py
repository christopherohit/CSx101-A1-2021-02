'''
Một phương trình đúng (PTĐ) được định nghĩa là phương trình có dạng a + b = c, trong đó a,b,c>0.

Ví dụ: phương trình 2 + 2 = 4 (| | + | | = | | | |) và 1 + 2 = 3 (| + | | = | | |) là PTĐ.

Còn 1 + 2 = 4 (| + | | = | | | |), 2 + 2 = 3 (| | + | | = | | |) và 0 + 1 = 1 ( + | = |) không phải là PTĐ.

Bây giờ bạn có 
n que diêm. Bạn muốn sử dụng tất cả số que diêm đó để xếp thành một PTĐ. Không may thay, 
có một số trường hợp bạn không thể xếp được nếu bạn dùng tất cả n que diêm. 
Nhưng nếu bạn ra chợ mua thêm k que diêm nữa thì bạn có thể xếp được.

Ví dụ, 
n=2, bạn cần mua thêm 2 cây diêm nữa để xếp thành | + | = | |.
n=5, bạn cần mua thêm 1 cây diêm nữa để xếp thành | | + | = | | |.                         

Nhiệm vụ của bạn là tìm ra số que diêm cần mua ít nhất để có thể xếp thành PTĐ.

INPUT:
Dòng đầu tiên là một số nguyên q (1≤q≤100) — số lượng testcase. 
q dòng tiếp theo, mỗi dòng là một số nguyên n(2≤n≤10^9) — số lượng que diêm có ban đầu.

OUTPUT:

Với mỗi testcase xuất ra trên một dòng số lượng que diêm tối thiểu cần phải mua để có thể xếp thành PTĐ.

VÍ DỤ:

INPUT       OUTPUT

4
2           2
5           1
8           0
11	        1
'''


def Xuly(i):
    if i == 2 :
        print(2)
    elif i % 2 == 0:
        print(0)
    elif i % 2 != 0 :
        print(1)



n = int(input())

for i in range(n):
    i = int(input())
    Xuly(i)

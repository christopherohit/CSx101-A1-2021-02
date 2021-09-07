'''
Cho một bàn cờ có kích thước n x n. Mỗi hàng được đánh số từ 1 đến n (từ dưới lên trên). 
Mỗi cột được đánh số từ 1 đến n (từ trái qua phải). Vì vậy, mỗi ô trong bàn cờ sẽ có tọa độ là (r,c) 
với r là vị trí của hàng, c là vị trí của cột.

Vua trắng bắt đầu từ vị trí (1,1) còn Vua đen bắt đầu từ vị trí (n,n). 
Một kho báu xuất hiện ngẫu nhiên ở vị trí (x,y) trong bàn cờ. 
Mỗi vị Vua sẽ tìm cách đến vị trí của kho báu đó, ai tới trước sẽ giành chiến thắng.

Tương tự như cờ vua, Vua trắng sẽ đi trước rồi tới lượt Vua đen và cứ thế luân phiên nhau. 
Mỗi lần chỉ được di chuyển đến ô liền kề nó nhất. Nếu Vua đang ở vị trí (a,b) thì có thể di chuyển 
đến một trong các vị trí (a+1,b), (a−1,b), (a,b+1), (a,b−1), (a+1,b−1), (a+1,b+1), (a−1,b−1), hoặc (a−1,b+1). 
Tất nhiên không được di chuyển ra khỏi bàn cờ.

Điểm khác biệt là các vị vua có thể đứng ở những vị trí kế nhau hoặc thậm chí là trùng vị trí với nhau.
Người chiến thắng là người đến vị trí kho báu đầu tiên. Bạn hãy xác định người chiến thắng.

INPUT:

Dòng đầu tiên là một số nguyên n (2≤n≤10^18) — kích thước của bàn cờ.
Dòng thứ hai gồm hai số x,y (1≤x,y≤n) — Tọa độ xuất hiện của kho báu.

OUTPUT:

Nếu Vua trắng thắng, xuất White

Ngược lại xuất Black
'''


n = int(input())
x , y = [int(x) for x in input().split()]

#if n % 2 != 0:
if ( x  < (n // 2) + 2 and y <= (n//2)):
    print("White")

elif (y <= (n//2) + 2 and x <= (n//2)):
    print("White")

else:
    if (x == 1  and y == 1):
        print("White")
    else:
        print("Black")
#else:
#    if x <= n / 2 + 1  
n = int(input())
a = str(n)
stra = ""

# Khử số 0 sau cùng
while (a[len(a)-1] == '0'):
    a = int(a)// 10
    a = str(a)

# Đảo Ngược chuổi
for i in range(len(a),0,-1):
    stra += a[i-1]
print(stra)
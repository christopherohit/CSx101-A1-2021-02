'''
Kiểm tra Số Armstrong (Số Armstrong là số có K chữ số và tổng lũy thừa bậc K của các chữ số bằng chính nó)

INPUT
Một số nguyên không âm

OUTPUT
Xuất True nếu số nhập vào là số Armstrong, ngược lại False
'''




def Check(n):
    sum = 0
    d = 0
    tempx = n
    p = len(str(n))
    while tempx > 0:
        d = tempx % 10
        sum = sum + pow(d,p)
        tempx = tempx//10
    if (sum == n):
        print(True)
    else:
        print(False)


n = int(input())
Check(n)
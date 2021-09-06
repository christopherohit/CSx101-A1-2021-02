# m ,n = [int(x) for x in input().split(" ")]

'''
Viết chương trình tính lũy thừa của hai số nguyên dương

INPUT
Hai số nguyên m và n

OUTPUT
Số dư còn lại khi lấy lũy thừa mn chia cho giá trị 1.000.000.007
'''



m , n = list(map(int,input().split()))
c = 1000000007
kq = pow(m,n,c)
print(kq)

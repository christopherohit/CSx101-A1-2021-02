'''
Đệ quy tính số Fibonacci thứ N

INPUT
Một số nguyên N

OUTPUT
Số Fibonacci thứ N
'''




def Fibonacci(x):
    if x < 0:
        return -1
    elif x <= 2:
        return 1
    else:
        return Fibonacci(x -1) + Fibonacci(x - 2)

n = int(input())
print(Fibonacci(n))
'''
Đệ quy tính N!

INPUT
Một số nguyên N không âm

OUTPUT
Giai thừa của N
'''

def Recurrent(n):
    if(n <= 0):
        return 1
    else:
        if n == 1:
            return n
        else:
            return n * Recurrent(n -1)



n = int(input())
print(Recurrent(n))

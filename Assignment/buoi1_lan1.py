'''
Viết chương trình nhập 2 số nguyên a và b.

In ra màn hình số lớn nhất, nhỏ nhất trong 2 số nguyên a và b vừa nhập.

Gợi ý: Có thể áp dụng công thức sau để tìm max, min giữa 2 số nguyên.

max=((a+b)+|a−b|)/2

min=(a+b)−|a−b|/2

Input:

Hai số nguyên a, b
Output:

Số lốn nhất (max) và số nhỏ nhất (min) trong 2 số nguyên a, b theo quy ước
'''



a, b = list(map(int,input().split()))


max = ((a+b) + abs(a-b))/2
min = ((a+b) - abs(a-b))/2

print ("max =", int(max))
print ("min =", int(min))
from fractions import Fraction

n = int(input())

sum = 0

for i in range(2 , n+1):
    sum += Fraction(1,i)

c = sum.denominator
b = sum.numerator
print("{:.4f}".format(b/c))

s1 , s2 , s3 = [int(x) for x in input().split()]
a = pow(s1*s2*s3, 1/2)*(1/s1+1/s2+1/s3)*4
print(round(a))
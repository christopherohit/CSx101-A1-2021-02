'''
Bình vừa mua xách tay một cái nhiệt kế hồng ngoại cực xịn cực chính xác chỉ mỗi tội nó hiển thị 
nhiệt độ theo thang đo độ F - Farenheit. Hãy giúp Bình đổi qua độ C - Celsius và độ K - Kelvin

INPUT
Một con số - nhiệt độ theo thang F

OUTPUT
Hai con số - nhiệt độ theo thang C và thang K
'''


#Transfer to C and K
from decimal import *




c = float(input())
Pc = ((c-32) * (5/9))
Pk = float(273.15 + Pc)

getcontext().prec = 6

print(Decimal(Pc).normalize() , round(Pk,3))

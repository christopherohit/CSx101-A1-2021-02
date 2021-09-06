'''
Tìm ra áp suất chất lỏng/khí và cách đo đạt chúng là một vấn đề nghiên cứu vật lý thực nghiệm từng làm đau đầu nhiều nhà khoa học thời trung cổ. Đã có nhiều nhà khoa học khác nhau đề xuất các thang đo khác nhau. Tuy nhiên ngày nay một đơn vị đo áp suất phổ thông mà dễ hiểu là tính lực tác động (theo khối lượng) chia cho diện tích. Khổ nổi trong hệ đo lường quốc tế (SI) và hệ đo Imperial phổ biến ở Mỹ người ta đo khối lượng và áp suất bằng cách đơn vị khác nhau. Bạn Bình vừa mua một con mô-tô phân khối lớn hàng nhập nguyên chiếc từ Mỹ về, tài liệu hướng dẫn của xe ghi áp suất phù hợp khi bơm xe bằng đơn vị PSI (Pound / square inches - 1 pound lực trên một inch vuông). Còn ống bơm của Bình tích hợp đồng hồ đo áp suất bằng đơn vị kg/cm2 (1 kilogram lực trên một centimét vuông).

Biết: 1 pound = 0.453592 kg

và 1 inch = 2,54 cm

Viết công thức giúp Bình đổi PSI sang kg/cm2

INPUT
Một con số duy nhất theo đơn vị PSI

OUTPUT
Một con số ương ứng theo đơn vị kg/cm2

'''


from decimal import *


a = float(input())
b = float(a * 0.0703069)
getcontext().prec = 6

print(Decimal(b).normalize())
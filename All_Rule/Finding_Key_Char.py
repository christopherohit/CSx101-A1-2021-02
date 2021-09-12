
#Trans String to Char to avoid Exception
n = 1

a ,b = [str(x) for x in input().split()]

# Cho chạy từ a -> b biến đổi nó thành số trong bản mã ASCII
for i in range(ord(a),ord(b)+1):
    # Từ mã ASCII biến đổi trở lại thành ký tự
    b = chr(i)
    print(b.upper(),end=" ")
#Version cuc suc

h, = input()
h = float(h)
result = []

for i in range(1,10):
    cal = (h -i)*2
    if cal == 2:
        result.append(cal)
        break
    result.append(cal)
print(round(sum(result)))

while True:
    try:
        n = str(input())    
        if int(n) <= 10:
            print("NO")
        else:
            print("{}".format("YES" if n[0] == n[-1] else "NO"))
    except EOFError:
        break
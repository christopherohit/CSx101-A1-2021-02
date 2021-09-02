def Tinhtoan(n , k):
    for i in k:
        pass

n = int(input())
while(True):
    k = int(input())
    p = int(input())
    q = int(input())
    if(k < 2 or k > n or p < 1 or p > (n + 1)/2 or q < 1 or q > 2):
        if (k == n + 1):
            print("No Solution Because This Test Have "+ k + " topic for "+ n + " student" )
            continue
        elif (k < 2 ):
            print("Math Error it have many solution for This question");
            continue
        else:
            print("Error or Wrong something which is incorrect to condition of Threads");
            
    else:
        pass
        



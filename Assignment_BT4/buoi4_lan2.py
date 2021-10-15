'''
Viết chương trình nhập vào một dãy gồm n số và biến k. Đếm số lần xuất hiện của k trong dãy đó. 

 INPUT: Dòng đầu tiên gồm một số nguyên dương q — số lượng testcase. Theo sau mỗi testcase gồm:

Dòng thứ nhất là hai số nguyên dương 
n,k   (1≤n≤1000),(−10^5≤k≤10^5) — Số phần tử của dãy và giá trị cần tìm vị trí.

Dòng thứ hai là giá trị các phần tử trong dãy a1,a2,...,an      (−10^5≤ai≤10^5)

OUTPUT: Ứng với mỗi testcase, xuất ra trên một dòng số lần xuất hiện của k.
'''
temp = int(input())


trys = 0
while trys <temp:
    n ,k = list(map(int,input().split()))
    a = []
    a[0:k] = [k for k in input().split()]
    trys +=1
    cout = 0
    for i in a:
        if str(i) == str(k):
            cout += 1
    print(cout)
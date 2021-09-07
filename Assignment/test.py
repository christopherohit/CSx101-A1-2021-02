import numpy as np

def calcCumulativeSum(arr):
    l = np.cumsum(arr)
    return l

arr = [10,20,30,40,50]
print(calcCumulativeSum(arr))
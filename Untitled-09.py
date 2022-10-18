def LargeSmallSum(arr):
    return sorted(arr[0::2])[-2]+sorted(arr[1::2])[1]


arr = [3, 2, 1, 7, 5, 4]
print(LargeSmallSum(arr))

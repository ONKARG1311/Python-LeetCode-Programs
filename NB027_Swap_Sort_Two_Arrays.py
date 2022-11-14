class Solution:
    def Rsort(self, arr1, arr2):
        nswap, swap = 0, 1
        for i in range(1, len(arr1)):
            if max(arr1[i - 1], arr2[i - 1]) < min(arr1[i], arr2[i]):
                nswap = min(nswap, swap)
                swap = nswap + 1
            elif arr1[i - 1] < arr1[i] and arr2[i - 1] < arr2[i]:
                swap += 1
            else:
                nswap, swap = swap, nswap + 1
        return min(nswap, swap)


if __name__ == "__main__":
    arr1 = [2, 1, 6, 5, 8]
    arr2 = [0, 3, 4, 7, 9]
    obj = Solution()
    x = obj.Rsort(arr1, arr2)
    print(x)

class Solution:
    def LargeSmallSum(self, arr: list[int]) -> int:
        return sorted(arr[0::2])[-2]+sorted(arr[1::2])[1]


if __name__ == "__main__":
    arr = [3, 2, 1, 7, 5, 4]
    obj = Solution()
    x = obj.LargeSmallSum(arr)
    print(x)

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = 1
        nums2 = sorted(list(set([x for x in nums if x > 0])))
        for i in range(len(nums2)):
            if (i+1) != nums2[i]:
                return i+1
        return len(nums2)+1


if __name__ == "__main__":
    nums = range(100)
    obj = Solution()
    x = obj.firstMissingPositive(nums)
    print(x)

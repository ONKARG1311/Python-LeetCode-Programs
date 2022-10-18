class Solution:
    def firstMissingPositive(nums) -> int:
        n = 1
        nums2 = sorted(list(set([x for x in nums if x > 0])))
        for i in range(len(nums2)):
            if (i+1) != nums2[i]:
                return i+1
        return len(nums2)+1


x = Solution.firstMissingPositive(range(1000000))
print(x)

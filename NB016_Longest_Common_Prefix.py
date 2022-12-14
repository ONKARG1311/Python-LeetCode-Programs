class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        temp = strs[0]
        for i in strs:
            while not i.startswith(temp):
                temp = temp[:-1]
        return temp


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    obj = Solution()
    x = obj.longestCommonPrefix(strs)
    print(x)

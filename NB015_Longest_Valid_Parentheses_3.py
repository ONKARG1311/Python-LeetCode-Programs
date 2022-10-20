class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return max(self.longestParentheses(s), self.longestParentheses(s[::-1]))

    def longestParentheses(self, s: str) -> int:
        ml = l = r = 0
        for i in s:
            if i == '(':
                l += 1
            else:
                r += 1
            if l == r:
                ml = max(ml, l*2)
            elif r > l:
                l = r = 0
        return ml


if __name__ == "__main__":
    s = "))()()(())"
    obj = Solution()
    x = obj.longestValidParentheses(s)
    print(x)

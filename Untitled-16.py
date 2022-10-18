class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return max(self.longestParentheses(self, s), self.longestParentheses(self, s[::-1]))

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


s = ")()"
x = Solution.longestValidParentheses(Solution, s)
print(x)

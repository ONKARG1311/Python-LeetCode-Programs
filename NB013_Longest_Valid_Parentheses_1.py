class Solution:
    def longestValidParentheses(self, s: str) -> int:
        self.len = 0
        for i in range(len(s)):
            for j in range(i, len(s)+1, 2):

                if self.ValidParentheses(s[i:j]):
                    if len(s[i:j]) > self.len:
                        self.len = len(s[i:j])
                else:
                    continue
        return self.len

    def ValidParentheses(self, s: str) -> bool:
        if len(s) == 0 or s.count("(") != s.count(")"):
            return False
        else:
            lc = rc = 0
            for i in s:
                if i == "(":
                    lc += 1
                else:
                    rc += 1
                if rc > lc:
                    return False
            return True


if __name__ == "__main__":
    s = "))()()(())"
    obj = Solution()
    x = obj.longestValidParentheses(s)
    print(x)

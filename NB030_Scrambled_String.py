class Solution:
    def isScramble(self, s, t, memo=dict()):

        if len(s) != len(t) or sorted(s) != sorted(t):
            return False
        if len(s) <= len(t) <= 1:
            return s == t
        if s == t:
            return True
        if (s, t) in memo:
            return memo[s, t]

        n = len(s)
        for i in range(1, n):
            a = self.isScramble(s[:i], t[:i], memo)\
                and self.isScramble(s[i:], t[i:], memo)
            if not a:
                b = self.isScramble(s[:i], t[-i:], memo)\
                    and self.isScramble(s[i:], t[:-i], memo)
            if a or b:
                memo[s, t] = True
                return True

        memo[s, t] = False
        return False


if __name__ == "__main__":
    s1 = "great"
    s2 = "rgeat"
    obj = Solution()
    z = obj.isScramble(s1, s2)
    print(z)

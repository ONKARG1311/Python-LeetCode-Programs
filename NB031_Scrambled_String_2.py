from functools import lru_cache


class Solution:
    @lru_cache(None)
    def isScramble(self, s, t):

        if len(s) != len(t) or sorted(s) != sorted(t):
            return False
        if len(s) <= len(t) <= 1:
            return s == t
        if s == t:
            return True

        n = len(s)
        for i in range(1, n):
            a = self.isScramble(s[:i], t[:i])\
                and self.isScramble(s[i:], t[i:])
            if not a:
                b = self.isScramble(s[:i], t[-i:])\
                    and self.isScramble(s[i:], t[:-i])
            if a or b:
                return True
        return False


if __name__ == "__main__":
    s1 = "great"
    s2 = "rgeat"
    obj = Solution()
    z = obj.isScramble(s1, s2)
    print(z)

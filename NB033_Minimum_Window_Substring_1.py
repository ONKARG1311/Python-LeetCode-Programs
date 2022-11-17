from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, l, r, i, j, missing = Counter(t), 0, 0, 0, 0, len(t)

        while r < len(s):
            if need[s[r]] > 0:
                missing -= 1
            need[s[r]] -= 1
            r += 1

            while missing == 0:
                if j == 0 or r-l < j-i:
                    i, j = l, r
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1

        return s[i:j]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    obj = Solution()
    z = obj.minWindow(s, t)
    print(z)

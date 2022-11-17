from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)

        for c in t:
            d[c] += 1

        n, output, l, count = len(d), str(), 0, 0

        for r in range(len(s)):
            d[s[r]] -= 1
            if d[s[r]] == 0:
                count += 1

            while count == n:
                if not output or len(output) > r - l + 1:
                    output = s[l:r+1]
                d[s[l]] += 1
                if d[s[l]] == 1:
                    count -= 1
                l += 1

        return output


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    obj = Solution()
    z = obj.minWindow(s, t)
    print(z)

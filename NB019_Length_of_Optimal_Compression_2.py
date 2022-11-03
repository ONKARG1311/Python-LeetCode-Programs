from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def counts(k, i, j, c):
            if k < 0:
                return n
            if i >= n:
                return 0
            if 0 <= j < n and s[i] == s[j]:
                return int(c == 1 or c == 9 or c == 99) + counts(k, i + 1, i, c + 1)
            return min(1 + counts(k, i + 1, i, 1), counts(k - 1, i + 1, j, c))

        return counts(k, 0, -1, 0)


if __name__ == "__main__":
    s = "aaaaaaaaaaa"
    k = 0
    obj = Solution()
    x = obj.getLengthOfOptimalCompression(s, k)
    print(x)

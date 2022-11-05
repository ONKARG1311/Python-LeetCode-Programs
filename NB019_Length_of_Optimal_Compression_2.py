from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(i, pvv, pvc, k):
            if k < 0 or i >= n:
                return {i >= n: 0, k < 0: n}[True]

            delete = dp(i + 1, pvv, pvc, k - 1)
            keep = (dp(i + 1, pvv, pvc + 1, k) + int(pvc in (1, 9, 99))
                    if s[i] == pvv else dp(i + 1, s[i], 1, k) + 1)

            return min(delete, keep)
        return dp(0, "", 0, k)


if __name__ == "__main__":
    s = "abc"
    k = 1
    obj = Solution()
    x = obj.getLengthOfOptimalCompression(s, k)
    print(x)

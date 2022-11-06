from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @lru_cache(None)
        def counts(skip, cvp, pvp, pvc):
            if skip < 0 or cvp >= n:
                return {cvp >= n: 0, skip < 0: n}[True]

            if 0 <= pvp < n and s[cvp] == s[pvp]:
                return int(pvc in (1, 9, 99)) + counts(skip, cvp + 1, cvp, pvc + 1)
            return min(1 + counts(skip, cvp + 1, cvp, 1), counts(skip - 1, cvp + 1, pvp, pvc))

        return counts(k, 0, -1, 0)


if __name__ == "__main__":
    s = "aaaaaaaaaaa"
    k = 0
    obj = Solution()
    x = obj.getLengthOfOptimalCompression(s, k)
    print(x)

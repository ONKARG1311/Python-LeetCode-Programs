class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] += dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    s = "rabbbit"
    t = "rabbit"
    obj = Solution()
    x = obj.numDistinct(s, t)
    print(x)

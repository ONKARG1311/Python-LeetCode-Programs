class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s


if __name__ == "__main__":
    s = "abcd"
    obj = Solution()
    z = obj.shortestPalindrome(s)
    print(z)

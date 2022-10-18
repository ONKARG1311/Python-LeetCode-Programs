class Solution:
    def longestPalindrome(s):
        x = [s[i: j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        y = [k for k in x if k == k[::-1]]
        z = [len(k) for k in y]
        w = z.index(max(z))
        return y[w]


s = "babad"
x = Solution.longestPalindrome(s)
print(x)

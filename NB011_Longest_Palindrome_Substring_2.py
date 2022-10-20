class Solution:
    def longestPalindrome(self, s: str) -> str:

        self.start = 0
        self.length = 0

        for i in range(len(s)):
            for j in range(min([i, len(s)-i-1])+1):
                temp = s[i-j:i+j+1]
                if temp == temp[::-1] and len(temp) > self.length:
                    self.start = i-j
                    self.length = len(temp)
                elif temp != temp[::-1]:
                    break

        for i in range(len(s)-1):
            for j in range(min([i, len(s)-i-2])+1):
                temp = s[i-j:i+j+2]
                if temp == temp[::-1] and len(temp) > self.length:
                    self.start = i-j
                    self.length = len(temp)
                elif temp != temp[::-1]:
                    break

        return s[self.start:self.start+self.length]


if __name__ == "__main__":
    s = "cbbd"
    obj = Solution()
    x = obj.longestPalindrome(s)
    print(x)

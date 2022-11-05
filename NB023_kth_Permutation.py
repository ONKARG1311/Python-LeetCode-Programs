class Solution:
    def getPermutation(self, n, k):
        num, output = list(range(1, n+1)), ""
        k -= 1

        while n > 0:
            n -= 1
            j, k = divmod(k, self.factorial(n))
            output += str(num[j])
            num.remove(num[j])

        return output

    def factorial(self, n):
        return (1 if n in (0, 1) else n * self.factorial(n - 1))


if __name__ == "__main__":
    n = 4
    k = 9
    obj = Solution()
    x = obj.getPermutation(n, k)
    print(x)

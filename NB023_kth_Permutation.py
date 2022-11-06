from math import factorial


class Solution:
    def getPermutation(self, n, k):
        num, output, k = list(range(1, n+1)), "", k-1

        while n > 0:
            n -= 1
            j, k = divmod(k, factorial(n))
            output += str(num[j])
            num.pop(j)

        return output


if __name__ == "__main__":
    n, k = 4, 9
    obj = Solution()
    x = obj.getPermutation(n, k)
    print(x)

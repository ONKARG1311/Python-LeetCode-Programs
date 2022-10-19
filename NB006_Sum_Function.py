class Solution:
    def sumFun(self, n: int, m: int) -> int:
        x = [i for i in range(1, m+1) if i % n == 0]
        y = [i for i in range(1, m+1) if i % n != 0]
        return abs(sum(x)-sum(y))


if __name__ == "__main__":
    n = 4
    m = 20
    obj = Solution()
    x = obj.sumFun(n, m)
    print(x)

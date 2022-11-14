class Solution:
    def MissingDigitII(self, strParam):
        x = strParam.split("=")

        for i in range(10):
            for j in range(10):
                m = eval(x[0].replace("?", str(i)))
                n = eval(x[1].replace("?", str(j)))
                if m == n:
                    print(i, " ", j, sep="")


if __name__ == "__main__":
    s = "38?5*3 = 1?595"
    obj = Solution()
    z = obj.MissingDigitII(s)

class Solution:
    def myAtoi(self, s: str) -> int:
        self.temp = s.strip()
        self.sign = "+"
        self.num = ""

        if self.temp == "":
            return 0

        if self.temp[0] == "+" or self.temp[0] == "-":
            self.sign = self.temp[0]
            self.temp = self.temp[1:]

        for i in range(len(self.temp)):
            if self.temp[:i+1].isdigit():
                self.num = self.temp[:i+1]
            else:
                break
        self.num = self.num.lstrip("0")
        if self.num == "":
            self.num = 0
        else:
            self.num = eval(self.sign+self.num)

        if self.num < -2147483648:
            self.num = -2147483648
        elif self.num > 2147483647:
            self.num = 2147483647

        return self.num


s = "  -42"
x = Solution.myAtoi(Solution, s)
print(x)

class Solution:
    def stringEvaluation(self, s: str) -> int:
        temp = s.replace("A", '&').replace("B", '|').replace("C", '^')
        value = eval(temp[0])
        for i in range(1, len(temp), 2):
            value = eval(str(value)+temp[i:i+2])
        return value


if __name__ == "__main__":
    s = "1C0C1C1A0B1"
    obj = Solution()
    x = obj.stringEvaluation(s)
    print(x)

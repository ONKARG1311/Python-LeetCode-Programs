class Solution:
    def isNumber(self, s: str) -> bool:

        try:
            float(s)
        except ValueError:
            return False
        else:
            if s in ("inf", "-inf", "+inf", "Infinity", "-Infinity", "+Infinity"):
                return False
            return True


if __name__ == "__main__":
    s = "-10"
    obj = Solution()
    x = obj.isNumber(s)
    print(x)

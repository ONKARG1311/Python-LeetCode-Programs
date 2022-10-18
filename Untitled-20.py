from itertools import combinations


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        min = len(s)
        for i in combinations(s, len(s)-k):
            sum = str()
            for j in i:
                sum += j
            x = self.StringCompression(sum)
            if min > len(x):
                min = len(x)
        return min

    def StringCompression(self, s: str) -> str:
        temp = list()
        for i in s:
            if temp == list():
                temp.append((i, 1))
            elif i == temp[-1][0]:
                temp3 = temp.pop()
                temp.append((i, temp3[1]+1))
            else:
                temp.append((i, 1))

        sum = str()
        for i in temp:
            if i[1] != 1:
                sum += str(i[0])+str(i[1])
            else:
                sum += str(i[0])

        return sum


if __name__ == "__main__":
    s = "aaaaaaaaaaa"
    k = 0
    obj = Solution()
    x = obj.getLengthOfOptimalCompression(s, k)
    print(x)

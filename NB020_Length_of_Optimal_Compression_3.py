class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        if s.strip() == str():
            return 0

        temp = list()
        for i in range(len(s)):
            if temp == list():
                temp.append(1)
            elif s[i] == s[i-1]:
                temp.append(temp.pop()+1)
            else:
                temp.append(1)
        temp.sort()

        sum = k
        for i in range(len(temp)):
            if sum >= temp[i]:
                sum -= temp[i]
                temp[i] = 0
            else:
                temp[i] -= sum
                break

        sum = 0
        for i in temp:
            if i == 1:
                sum += 1
            elif i > 1:
                sum += len(str(i))+1

        return sum


if __name__ == "__main__":
    s = "aabbaa"
    k = 2
    obj = Solution()
    x = obj.getLengthOfOptimalCompression(s, k)
    print(x)

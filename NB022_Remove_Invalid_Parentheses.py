class Solution:
    def removeInvalidParentheses(self, s):
        if len(s) == 0:
            return list()

        visit, queue, output, level = {s}, [s], list(), False

        while (len(queue)):
            str = queue.pop(0)
            if self.validParentheses(str):
                output.append(str)
                level = True

            if level:
                continue

            for i in range(len(str)):
                if str[i] not in ('(', ')'):
                    continue

                temp = str[:i] + str[i+1:]
                if temp not in visit:
                    visit.add(temp)
                    queue.append(temp)

        return output

    def validParentheses(self, s: str) -> bool:
        count = 0
        for i in s:
            if i in ('(', ')'):
                count = count + (1 if i == '(' else -1)
            if count < 0:
                return False
        return count == 0


if __name__ == "__main__":
    s = "(a)())()"
    obj = Solution()
    x = obj.removeInvalidParentheses(s)
    print(x)

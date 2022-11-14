from collections import defaultdict


class Solution:
    def expendicture(self, A, D):
        n, d = len(A), defaultdict(list)

        for i in range(n):
            d[D[i][5:7]].append(A[i])

        count = 0
        for i in d:
            temp = [-x for x in d[i] if x < 0]
            if sum(temp) >= 100 and len(temp) >= 3:
                count += 1

        return sum(A)+(count-12)*5


if __name__ == "__main__":
    A = [100, 100, 100, -10]
    D = ['2020-12-31', '2020-12-22', '2020-12-03', '2020-12-29']
    obj = Solution()
    x = obj.expendicture(A, D)
    print(x)

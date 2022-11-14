class Solution:
    def EightQueens(self, strArr):
        arr = [(eval(x)[0]-1, eval(x)[1]-1) for x in strArr]
        mat = [[0]*8 for i in range(8)]

        for i in range(8):
            for j in range(8):
                if (i, j) in arr:
                    mat[i][j] = 1

        return self.validQueens(mat)

    def validQueens(self, mat):
        n = len(mat)
        r, c, d1, d2 = set(), set(), set(), set()

        for i in range(n):
            for j in range(n):
                if mat[i][j]:
                    r.add(i)
                    c.add(j)
                    d1.add(i - j)
                    d2.add(i + j)

        return len(r) == len(c) == len(d1) == len(d2) == n


if __name__ == "__main__":
    s = ["(2,1)", "(4,2)", "(6,3)", "(8,4)",
         "(3,5)", "(1,6)", "(7,7)", "(5,8)"]
    obj = Solution()
    z = obj.EightQueens(s)
    print(z)

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        output = list()

        def backtrack(pos, row):
            if len(pos) == row == n:
                output.append(pos)
            for col in range(n):
                if all(row != r and col != c and abs(row - r) != abs(col - c) for r, c in pos):
                    backtrack(pos + [(row, col)], row + 1)

        backtrack([], 0)
        return [[''.join('Q' if (i, j) in sol else '.' for i in range(n)) for j in range(n)] for sol in output]


if __name__ == "__main__":
    n = 4
    obj = Solution()
    z = obj.solveNQueens(n)
    print(z)

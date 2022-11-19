class Solution:
    def totalNQueens(self, n: int) -> int:

        def rec(col, horizontal, d1, d2):
            if col == n:
                return 1

            output = 0
            for row in range(n):
                if row not in horizontal and (row + col) not in d1 and (row - col) not in d2:
                    horizontal[row] = True
                    d1[row + col] = True
                    d2[row - col] = True

                    output += rec(col + 1, horizontal, d1, d2)

                    del horizontal[row]
                    del d1[row + col]
                    del d2[row - col]

            return output
        return rec(0, {}, {}, {})


if __name__ == "__main__":
    n = 4
    obj = Solution()
    z = obj.totalNQueens(n)
    print(z)

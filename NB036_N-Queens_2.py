class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        state = [["."] * n for _ in range(n)]
        res, vc, vd1, vd2 = list(), set(), set(), set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in state])

            for c in range(n):
                _diff = r-c
                _sum = r+c

                if not (c in vc or _diff in vd1 or _sum in vd2):
                    vc.add(c)
                    vd1.add(_diff)
                    vd2.add(_sum)
                    state[r][c] = 'Q'
                    backtrack(r+1)

                    vc.remove(c)
                    vd1.remove(_diff)
                    vd2.remove(_sum)
                    state[r][c] = '.'

        backtrack(0)
        return res


if __name__ == "__main__":
    n = 4
    obj = Solution()
    z = obj.solveNQueens(n)
    print(z)

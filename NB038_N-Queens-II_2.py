class Solution:
    def totalNQueens(self, n: int) -> int:
        state = [['.'] * n for _ in range(n)]
        output, visited_col, visited_d1, visited_d2 = set(), set(), set(), set()

        def backtrack(r):
            if r == n:
                output.add(map('#'.join, map(''.join, state)))
                return None

            for c in range(n):
                if not (c in visited_col or (r-c) in visited_d1 or (r+c) in visited_d2):
                    visited_col.add(c)
                    visited_d1.add(r-c)
                    visited_d2.add(r+c)
                    state[r][c] = 'Q'

                    backtrack(r+1)

                    visited_col.remove(c)
                    visited_d1.remove(r-c)
                    visited_d2.remove(r+c)
                    state[r][c] = '.'

        backtrack(0)
        return len(output)


if __name__ == "__main__":
    n = 4
    obj = Solution()
    z = obj.totalNQueens(n)
    print(z)

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, cur, n_letters = [], [], 0

        for w in words:
            if n_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - n_letters):
                    cur[i % (len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, n_letters = [], 0
            cur += [w]
            n_letters += len(w)

        return res + [' '.join(cur).ljust(maxWidth)]


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    obj = Solution()
    z = obj.fullJustify(words, maxWidth)
    print(z)

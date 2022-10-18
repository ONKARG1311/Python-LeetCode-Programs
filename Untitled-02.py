from itertools import permutations


class Solution:
    def findSubstring(s, words):
        x = set(["".join(i) for i in permutations(words)])
        pos = []
        for i in x:
            pos.extend([j for j in range(len(s)) if s.startswith(i, j)])
        return list(set(pos))


s = "aaa"
words = ["a", "a"]
m = Solution.findSubstring(s, words)
print(m)

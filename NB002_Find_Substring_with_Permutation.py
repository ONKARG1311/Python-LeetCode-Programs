from itertools import permutations


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        x = set(["".join(i) for i in permutations(words)])
        pos = []
        for i in x:
            pos.extend([j for j in range(len(s)) if s.startswith(i, j)])
        return list(set(pos))


if __name__ == "__main__":
    s = "aaa"
    words = ["a", "a"]
    obj = Solution()
    x = obj.findSubstring(s, words)
    print(x)

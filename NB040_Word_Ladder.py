from collections import defaultdict
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        L = len(beginWord)
        d = defaultdict(list)
        for w in wordList:
            for i in range(L):
                d[w[:i] + "*" + w[i+1:]].append(w)

        q, v = deque([(beginWord, 1)]), set()
        v.add(beginWord)

        while q:
            cw, level = q.popleft()

            for i in range(L):
                temp = cw[:i] + "*" + cw[i+1:]
                for w in d[temp]:
                    if w == endWord:
                        return level + 1
                    if w not in v:
                        v.add(w)
                        q.append((w, level + 1))
        return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    obj = Solution()
    z = obj.ladderLength(beginWord, endWord, wordList)
    print(z)

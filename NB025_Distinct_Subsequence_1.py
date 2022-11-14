class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        index = dict()
        counts = [1] + [0] * len(t)

        for i, c in enumerate(t):
            if c in index:
                index[c].append(i + 1)
            else:
                index[c] = [i+1]

        for c in s:
            for i in reversed(index[c]):
                counts[i] += counts[i - 1]

        return counts[-1]


if __name__ == "__main__":
    s = "rabbbit"
    t = "rabbit"
    obj = Solution()
    x = obj.numDistinct(s, t)
    print(x)

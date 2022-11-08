from collections import defaultdict


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        c_indices = defaultdict(list)
        max_counts = [1] + [0] * len(t)
        for i, c in enumerate(t):
            c_indices[c].append(i + 1)
        for c in s:
            for i in reversed(c_indices[c]):
                max_counts[i] += max_counts[i - 1]
        return max_counts[-1]


if __name__ == "__main__":
    s = "rabbbit"
    t = "rabbit"
    obj = Solution()
    x = obj.numDistinct(s, t)
    print(x)
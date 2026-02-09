class Solution:
    def minSteps(self, s: str, t: str) -> int:
        countS = Counter(s)

        for char in t:
            countS[char] = max(countS[char] - 1, 0)

        return sum(countS.values())
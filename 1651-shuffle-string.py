class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        result = [""] * n

        for i in range(n):
            index = indices[i]
            result[index] = s[i]

        return "".join(result)
        
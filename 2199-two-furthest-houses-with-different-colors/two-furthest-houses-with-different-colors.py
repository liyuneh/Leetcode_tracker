class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        mx = 0
        for i in range(len(colors)):
            dis = 0
            for j in range(len(colors) - 1, i, -1):
                if colors[i] != colors[j]:
                    mx = max(mx, abs(i - j))
        return mx
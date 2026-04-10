class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq = defaultdict(list)
        for i , ch in enumerate(nums):
            freq[ch].append(i)
        if not any(len(val) >= 3 for val in freq.values()):
            return -1
        mn = float("inf")
        for key , val in freq.items():
            if len(val) >= 3:
                for i in range(len(val) - 2):
                    x, y, z = val[i], val[i + 1], val[i + 2]
                    if abs(x-y) + abs(y- z) + abs(z - x) < mn:
                        mn =  abs(x-y) + abs(y- z) + abs(z - x) 
        print(mn)
        return mn
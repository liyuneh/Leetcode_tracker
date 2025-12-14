class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = {}
        for ch in nums:
            freq[ch] = freq.get(ch, 0) + 1
        count = 0
        if k == 0:
            for val in freq.values():
                if val > 1:
                    count += 1
        else:
            for key in freq:
                if key + k in freq:
                    count += 1
        return count
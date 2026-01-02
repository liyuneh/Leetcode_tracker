class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        freq = {}
        for ch in nums:
            freq[ch] = freq.get(ch, 0) + 1
        for key, val in freq.items():
            if val == n:
                return key
        
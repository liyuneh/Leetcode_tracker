class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total = (len(nums) * (len(nums) - 1)) // 2
        freq = defaultdict(int)
        count = 0
        for i , num in enumerate(nums):
            val = num - i
            count += freq[val]
            freq[val] += 1
        print(total - count)
        return total - count
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev (x):
            x = str(x)[::-1]
            return int(x)
        count = 0
        freq = defaultdict(int)
        for i ,ch in enumerate(nums):
            val = nums[i] - rev(nums[i])
            count += freq[val]
            freq[val] += 1
        return count % (10 ** 9 + 7)
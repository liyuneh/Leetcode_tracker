class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev (x):
            x = str(x)[::-1]
            return int(x)
        for i ,ch in enumerate(nums):
            nums[i] = nums[i] - rev(nums[i])
        freq = defaultdict(int)
        for ch in nums:
            freq[ch] += 1
        count = 0
        for ch in nums:
            freq[ch] -= 1
            count += freq[ch]
        return count % (10 ** 9 + 7)
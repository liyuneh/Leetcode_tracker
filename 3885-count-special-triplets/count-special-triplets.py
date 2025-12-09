class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        total = 0
        total_count = Counter(nums)
        cur_count = Counter()
        for i in range(len(nums)):
            left_count = cur_count[nums[i] * 2] 
            right_count = total_count[nums[i] * 2] - left_count - (not nums[i])
            total += left_count * right_count
            cur_count[nums[i]] += 1
        return total % (10**9 + 7)
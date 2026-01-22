class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0

        def sorted_ok(a):
            return all(a[i] <= a[i+1] for i in range(len(a) - 1))

        while not sorted_ok(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]
                if s < min_sum:
                    min_sum = s
                    idx = i

            nums = nums[:idx] + [min_sum] + nums[idx + 2:]
            ops += 1

        return ops

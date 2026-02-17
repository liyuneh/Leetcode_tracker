class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l , r = i + 1, len(nums) - 1

            while l < r:
                x = nums[i] + nums[l] + nums[r]

                if abs(target - x) < abs(target - close):
                    close = x
                if x == target:
                    return target
                elif x < target:
                    l += 1
                else:
                    r -= 1
        return close
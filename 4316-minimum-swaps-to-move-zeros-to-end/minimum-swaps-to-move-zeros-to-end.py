class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j] , nums[i]
                        count += 1
                        break
        print(count)
        return count
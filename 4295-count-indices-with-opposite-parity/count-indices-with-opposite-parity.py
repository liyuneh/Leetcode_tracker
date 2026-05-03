class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        ans = []

        for i in range(len(nums)):
            count = 0
            for j in range(i + 1, len(nums)):
                if nums[i] % 2 != nums[j] % 2:
                    count += 1
            ans.append(count)
        return ans
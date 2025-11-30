class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l , r = 0 , len(nums) - 1
        cur = 0
        while cur < r:
            if nums[cur] % 2 == 0:
                nums[cur], nums[l] = nums[l], nums[cur]
                cur +=1
                l += 1
            else:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1
        return nums
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        ans = [1] * n
        leftsum , rightsum = 1 , 1
        for i in range(n):
            ans[i] = leftsum
            leftsum *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            ans[j] *= rightsum
            rightsum *= nums[j]
        return ans

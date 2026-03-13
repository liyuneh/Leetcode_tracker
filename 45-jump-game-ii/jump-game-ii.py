class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ans=0
        opt = 0
        far= 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == opt:
                ans += 1
                opt = far
        
        return ans
            
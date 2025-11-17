class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 in nums:
            l = nums.index(1)
        else:
            return True
        for r in range(l + 1,len(nums)):
            if nums[r] == 1 :
                if r - l - 1 < k:
                    return False
                l = r
            
        return True
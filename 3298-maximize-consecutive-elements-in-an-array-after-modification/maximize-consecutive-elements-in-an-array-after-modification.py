from functools import cache
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)

        def find(index, target):
            x = bisect_left(nums, target, index)
            if x < n and nums[x] == target:
                return x
            return -1
        @cache
        def solve(index, inc):

            val = nums[index] + inc

            ans = 1

            j = find(index + 1 , val + 1)
            if j != -1:
                ans = max(ans, 1 + solve(j, 0))
            
            j = find(index + 1, val)
            if j != -1:
                ans = max(ans, 1 + solve(j, 1))
            
            return ans
        # nums.sort()
        res = 1
        for i in range(n):
            res = max(res, solve(i,0), solve(i, 1))

        # print(res)
       
        return res
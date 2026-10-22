class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0
        if len(nums) == 2 and nums != sorted(nums):
            return 1
        if reversed(nums) == sorted(nums):
            return 1
        mn = min(nums)
        k = 0
        for i in range(len(nums)):
            if nums[i] == mn:
                k = i
                break     
        ans = nums[:k ]
        ans.reverse()
        ans1 = nums[k + 1: ][::-1]
        classic = [0] + ans + ans1
        new =  [0] + ans1[::-1] + ans[::-1]
        # print(classic , new)
        if classic != sorted(classic) and new != sorted(new):
            return -1
        if classic == sorted(classic):
            return 1 + min(len(nums) - (k + 1), k + 1)
        if new == sorted(new) :
            cnt = 0
            for i in range(k , len(nums)):
                cnt += 1
            return min(len(nums) - cnt, 2 + cnt)
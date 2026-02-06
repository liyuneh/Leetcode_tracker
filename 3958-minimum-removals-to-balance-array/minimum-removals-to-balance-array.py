class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans , n = float('inf') , len(nums)

        for i in range(len(nums)):
            x =bisect_right(nums, nums[i] * k)
            # print(x)
            ans = min(ans, n - (x - i ))
        return ans
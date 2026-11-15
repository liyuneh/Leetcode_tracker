class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            mn = nums[i] 
            new = nums[i]
            for j in range(i , len(nums)):
                mn = min(mn, nums[j])
                new = new & nums[j]
                if new == mn:
                    ans += 1
        # print(ans)
        return ans
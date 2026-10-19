class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 1
        for start in range(n):
            for end in range(start, n):
                if nums[end] % k != nums[start] % k :
                    break
                
                m = end - start + 1
                if ((m - 1) * nums[start]) % k == 0 :
                    ans = max(ans, end - start + 1)
        # print(ans)
        return ans 
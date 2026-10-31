class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if sum(nums) % k == 0:
            return n
        ans = 0
        for i in range(n):
            curr = nums[i]
            mx  = 1 if nums[i] % k == 0 else 0
            seen = set()
            x =  - (nums[i] * 2)
            seen.add(x % k)
            for j in range(i + 1, n):
                curr += nums[j]
                z = -(nums[j] * 2)
                seen.add(z % k)
                if curr % k == 0 or k - (curr % k) in seen :
                    mx = max(mx, j - i + 1)
                # print(curr, k - (curr % k), mx)
            ans = max(ans, mx)
                
        
        # print(mx)


        return ans
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            takengcd, takenlcm= nums[i], nums[i]
            x = nums[i]
            for j in range(i+ 1, len(nums)):
                x *= nums[j]
                takengcd = math.gcd(takengcd,nums[j])
                takenlcm = math.lcm(takenlcm, nums[j])
                if x == takengcd *  takenlcm:
                    ans = max(ans, j - i + 1)
        # print(ans)
        return ans
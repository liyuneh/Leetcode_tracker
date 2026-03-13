class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans = []
        total = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= total :
                total += nums[i]
            else:
                ans.append(total)
                total = nums[i]
        if total :
            ans.append(total)
        # print(ans)

        return  max(ans)  
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        num = sorted(nums)
        ans = []
        for k in nums:
            ans.append(num.index(k))
        return ans
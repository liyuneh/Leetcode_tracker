class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        numss = sorted(nums)
        ans = []
        for num in nums:
            ans.append(numss.index(num))
        return ans
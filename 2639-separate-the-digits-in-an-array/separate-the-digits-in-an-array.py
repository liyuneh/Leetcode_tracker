class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i  in range(len(nums)):
            x = str(nums[i])
            for j in range(len(x)):
                ans.append(int(x[j]))
        return ans
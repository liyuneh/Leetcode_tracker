class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <2:
            return nums
        counter = Counter(nums)
        ans = []
        for key, value in  counter.items():
            if value > len(nums) // 3:
                ans.append(key)
        return ans
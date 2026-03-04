class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mn = float("inf")
        pref = 0
        for num in nums:
            pref += num
            mn = min(mn, pref)
            print(mn)
        return abs(mn)  + 1 if mn < 0 else 1

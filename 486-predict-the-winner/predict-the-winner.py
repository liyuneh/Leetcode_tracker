class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)

        def mx(l, r):
            if l > r:
                return 0
            left = nums[l] - mx(l + 1, r)
            right = nums[r] - mx(l, r - 1)

            return max(left,right)
        return mx(0,n-1) >= 0
        
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 0
        nums.sort()
        # print(nums)
        new, ans = [], []
        new = [nums[2] + 1, nums[2] + 1] + nums[2:]
        ans = [nums[-3], nums[-3]] + nums[:-2]
        third = [nums[1] + 1] + nums[1:-1] + [nums[-2]]
        third.sort()
        new.sort()
        ans.sort()
        lowt , hight = float('inf') , third[-1] - third[0]
        lown , highn = float('inf'), new[-1] - new[0]
        lowa, higha = float('inf'), ans[-1] - ans[0]
        for i in range(len(ans) - 1):
            lowa = min(lowa, ans[i + 1] - ans[i])
            lown = min(lown, new[i + 1] - new[i])
            lowt = min(lowt, third[i + 1] - third[i])
        mn = min(lown + highn, lowa + higha, hight + lowt)
        # print(mn)

        
        return mn
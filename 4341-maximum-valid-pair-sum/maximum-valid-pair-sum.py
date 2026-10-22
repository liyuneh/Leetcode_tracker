class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        if k == 1:
            mxa = max(nums)
            k = 0
            for i in range(len(nums)):
                if nums[i] == mxa:
                    k = i
                    break
            mx = 0
            for i in range(len(nums)):
                if i != k:
                    mx = max(mx, mxa + nums[i])
            return mx
        ans = []
        mx = 0
        for i in range(len(nums)):
            if nums[i] > mx :
                mx = nums[i]
            ans.append(mx)
        count = 0
        for i in range(len(nums)):
            if i >= k :
                count = max(count, nums[i] + ans[i - k] )
        print(count)

        return count
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        arr = [0] * (len(nums))
        for l , r in requests:
            arr[l] += 1
            if r + 1 < len(nums):
                arr[r+1] -= 1
        pref = 0
        for i in range(len(arr)):
            pref += arr[i]
            arr[i] = pref
        nums.sort(reverse = True)
        mx = 0
        arr.sort(reverse = True)
        for i in range(len(arr)):
            mx += (nums[i] * arr[i])
        print(mx)
        return mx % (10 ** 9 + 7)
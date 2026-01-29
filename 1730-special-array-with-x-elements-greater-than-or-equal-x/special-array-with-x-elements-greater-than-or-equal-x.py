class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        arr = [i for i in range(1, max(nums)+1)]
        print(arr)
        for i in range(len(arr)):
            x = bisect_left(nums,arr[i])
            # print(x)
            if len(nums) - x == arr[i]:
                return arr[i]
        return -1
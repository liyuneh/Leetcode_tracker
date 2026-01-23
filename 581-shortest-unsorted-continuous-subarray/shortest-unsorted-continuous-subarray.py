class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = -1, -1

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                left = i
                break

        if left == -1:
            return 0

        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                right = i
                break

        sub_min = min(nums[left:right + 1])
        sub_max = max(nums[left:right + 1])

        while left > 0 and nums[left - 1] > sub_min:
            left -= 1

        while right < n - 1 and nums[right + 1] < sub_max:
            right += 1

        return right - left + 1

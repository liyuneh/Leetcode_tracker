class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums) - 1
        while l <= r and nums[l] <= target <= nums[r] :
            if nums[l] == nums[r]:
                return l if nums[l] == target else -1
            mid = int(l + (r-l)* ((target - nums[l]) / (nums[r] - nums[l])))
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
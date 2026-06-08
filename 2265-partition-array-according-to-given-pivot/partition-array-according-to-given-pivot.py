class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        upper = []
        equal = []
        for i in range (len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] > pivot:
                upper.append(nums[i])
            else:
                equal.append(nums[i])
        return less + equal + upper
        
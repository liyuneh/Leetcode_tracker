class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            rightsum , leftsum = 0,0
            if nums[i] == 0:
                leftsum = sum(nums[:i])
                rightsum = sum(nums[i+1:])
                if rightsum == leftsum:
                    count += 2
                elif abs(rightsum - leftsum) == 1:
                    count += 1
        return count
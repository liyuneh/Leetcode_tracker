class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = 1
        new = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == new:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count += 1
                    new = nums[i]
        count = 0
        for i in range(len(nums)):
            if nums[i] == new:
                count += 1
        count1 = 0
        for i in range(len(nums)):
            if nums[i] == new:
                count1 += 1
                x = count - count1
                if count1 > (i+1) // 2 and x > (len(nums) - (i + 1)) // 2:
                    return i
        return -1
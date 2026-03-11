class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        cur = nums[0]
        for r in nums[1:]:
            while stack and r >= stack[-1][0]:
                stack.pop()
            if stack and r > stack[-1][1]:
                return True
            stack.append([r, cur])
            # print(stack)
            cur = min(cur , r)
        return False
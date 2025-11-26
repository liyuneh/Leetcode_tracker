class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []

        for c in nums:
            if not stack or c >= stack[-1]:
                stack.append(c)
        return len(stack)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        count = 0
        for c in nums:
            while stack and stack[-1] > c:
                stack.pop()
            if c > 0 and (not stack or stack[-1] < c):
                count += 1
                stack.append(c)
        return count
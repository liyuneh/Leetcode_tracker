class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum (nums)
        if total % 3 == 0:
            return total
        num1 = []
        num2 = []
        for r in nums:
            if r % 3 == 1:
                num1.append(r)
            elif r % 3 == 2:
                num2.append(r)
        num1.sort()
        num2.sort()
        if total % 3 == 1:
            op1 = num1[0] if num1 else float('inf')
            op2 = num2[0] + num2[1] if len(num2) >= 2  else float('inf')
            return total - min(op1, op2)

        elif total % 3 == 2:
            op1 = num2[0] if num2 else float('inf')
            op2 = num1[0] + num1[1] if len(num1) >= 2 else float('inf')
            return total - min(op1, op2)
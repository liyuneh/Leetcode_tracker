class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        if num1 == num2:
            return 1
        count = 0
        while num1 != num2:
            while num1 < num2:
                num2 -= num1
                count += 1
            while num1 > num2:
                num1 -= num2
                count += 1
        return count + 1

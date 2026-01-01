class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = digits.pop()
        if x + 1 <= 9:
            digits.append(x+1)
            return digits
        ans = [0]
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            digits.pop()
            ans.append(0)
            i -= 1
        if i >= 0:
            digits[-1] += 1
        else:
            ans.append(1)
        return digits + ans[::-1]
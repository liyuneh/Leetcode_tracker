class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        r = 0
        while r < n - 1:
            if bits[r] == 1:
                r += 2
            else:
                r += 1
        return r == n - 1  


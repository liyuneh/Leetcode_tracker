class Solution:
    def minimumFlips(self, n: int) -> int:
        a = bin(n)[2:]
        b = a[::-1]
        l , r = 0 , 0
        count = 0
        while l < len(a) and r < len(b):
            if a[l] != b[r]:
                count += 1
            l += 1
            r += 1
        
        return count
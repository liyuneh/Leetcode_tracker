class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10 
        can = True

        while n >= remove:
            n -= remove
            remove -= 1
            can = not can
        return not can
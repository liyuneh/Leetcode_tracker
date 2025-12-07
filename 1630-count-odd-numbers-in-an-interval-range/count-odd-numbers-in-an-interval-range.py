class Solution:
    def countOdds(self, low: int, high: int) -> int:
        countl = 0 if low % 2 == 0 else 1
        countr = 0 if high % 2 == 0 else 1
        if countr == countl == 1:
            return countl + countr + (high - low ) // 2 - 1
        elif countl != countr:
            return 1 + (high - low) // 2
        else:
            return (high - low) // 2
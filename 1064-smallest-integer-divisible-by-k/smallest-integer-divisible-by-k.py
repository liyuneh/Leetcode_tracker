class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return - 1
        seen = set()
        rem = 0
        leng = 0
        while rem not in seen:
            seen.add(rem)
            rem = (rem * 10 + 1) % k
            leng += 1
            if rem == 0:
                return leng
        return -1
        
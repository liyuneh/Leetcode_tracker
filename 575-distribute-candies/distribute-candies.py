class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        freq = {}
        for ch in candyType:
            freq[ch] = freq.get(ch , 0) + 1
        count = 0
        for _ in freq.values():
            count += 1
        max_allo = len(candyType) // 2

        return count if count < max_allo else max_allo
        
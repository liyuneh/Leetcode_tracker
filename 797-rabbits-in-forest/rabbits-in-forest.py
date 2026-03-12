class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = defaultdict(int)
        for ch in answers:
            freq[ch] += 1
        total = 0
        for key , val in freq.items():
            total += (math.ceil(val / (key + 1)) * (key+1))
        # print(total)
        return total 
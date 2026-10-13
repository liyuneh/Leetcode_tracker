class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        freq = defaultdict(int)
        prefix = [0] * len(capacity)
        total = 0
        for i , c in enumerate(capacity):
            total += c
            prefix[i] = total
        count = 0
        
        for i in range(2, len(capacity)):
            a = i - 2

            freq[(capacity[a], prefix[a])] += 1

            count += freq[(capacity[i], prefix[i] - 2 * capacity[i])]
        # print(count)
        return count
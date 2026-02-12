class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        counter_s1 = Counter(s1 + s2)
        for val in counter_s1.values():
            if val % 2 == 1:
                return -1
        res = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                res.append((s1[i], s2[i]))
        freq = defaultdict(int)
        for i in range(len(res)):
            freq[res[i]] += 1
        ans  = 2 if any(val % 2 == 1 for val in freq.values()) else 0
        for val in freq.values():
            if val % 2 == 0:
                ans += (val // 2)
            else:
                ans += (val - 1) // 2

        
        return ans

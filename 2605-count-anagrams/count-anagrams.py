from collections import defaultdict
class Solution:
    def countAnagrams(self, s: str) -> int:
        count = 1
        s = s.split()
        for i in range(len(s)):
            freq = defaultdict(int)
            for ch in s[i]:
                freq[ch] += 1
            n = len(s[i])
            sum1 = 1
            for val in freq.values():
                sum1 *= math.factorial(val)
            count *= (math.factorial(n) // sum1)
        return count % (10 ** 9 + 7)
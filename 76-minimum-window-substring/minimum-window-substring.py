class Solution:
    def minWindow(self, s: str, t: str) -> str:
        new = Counter()
        counter_t = Counter(t)

        mn_str = ""
        mn = float("inf")
        l = 0
        for i in range(len(s)):
            new[s[i]] += 1
            while counter_t <= new:
                if mn >= i - l + 1:
                    mn = i - l + 1
                    mn_str = s[l:i+1]
                new[s[l]] -= 1
                l += 1
        return mn_str
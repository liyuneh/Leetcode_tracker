class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = Counter()

        ans = 0
        l = 0
        max_freq = 0
        for i in range(len(s)):
            c[s[i]] += 1
            max_freq = max(max_freq , c[s[i]])

            while (i - l + 1) - max_freq > k:
                c[s[l]] -= 1
                l += 1
            ans = max(ans, i - l + 1)
        # print(ans)
        return ans
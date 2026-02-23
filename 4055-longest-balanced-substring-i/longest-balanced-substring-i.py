class Solution:
    def longestBalanced(self, s: str) -> int:
        mx = 0
        for i in range(len(s)):
            b = 0
            ans = defaultdict(int)
            for j in range(i, len(s)):
                ans[s[j]] += 1
                if all (val == ans[s[j]] for val in ans.values()):
                    b = max(b , j - i + 1)
            mx = max(mx, b)

        # print(mx)
        return mx
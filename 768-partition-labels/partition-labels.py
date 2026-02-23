class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mn = 0
        ans = []
        m = 1
        for i in range(len(s)):
            x = s.rindex(s[i]) + 1
            mn = max(mn , x)
            if mn - i - 1   == 0:
                ans.append(mn - m)
                m = mn
        ans[0] = ans[0] + 1
        return  ans
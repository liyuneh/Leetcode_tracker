class Solution:
    def minOperations(self, s: str) -> int:
        if "".join(sorted(s)) == s:
            return 0
        if len(s) == 2 and "".join(sorted(s)) != s:
            return -1
        ans = [ord(x) for x in s]
        l ,r, mx = 0 ,0, 0
        mn = float("inf")
        # print(ans)
        for i, x in enumerate(ans):
            if mx <= x:
                mx = x
                r = i
            if x < mn:
                mn = x
                l = i
        if (ans[-1] == mx ) or (ans[0] == mn):
            return 1
        if l + 1 == len(ans) and r == 0 :
            return 3
        return 2
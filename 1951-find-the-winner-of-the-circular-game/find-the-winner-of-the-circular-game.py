class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def rec(ans,x):
            if len(ans) == 1:
                return ans[0]
            x = (x + k - 1) % len(ans)
            ans.pop(x)
            return rec(ans, x)

        return rec([i + 1 for i in range( n)], 0)

            
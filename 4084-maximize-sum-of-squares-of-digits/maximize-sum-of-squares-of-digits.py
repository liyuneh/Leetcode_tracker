class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        ans = []
        if sum > num * 9:
            return ""
        while sum > 9:
            ans.append("9")
            sum -= 9
        if sum:
            ans.append(str(sum))

        if len(ans) == num:
            return "".join(ans)
        else:
            x = num - len(ans)
            for i in range(x):
                ans.append("0")
            return "".join(ans)
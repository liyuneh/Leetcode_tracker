class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def total (n):
            ans = [int(m) for m in str(n)]
            count = 0
            for i in range(1, len(ans) - 1):
                if ans[i-1] < ans[i]  and ans[i] > ans[i + 1]:
                    count += 1
            for i in range(1, len(ans) - 1):
                if ans[i-1] > ans[i] and ans[i] < ans[i + 1]:
                    count += 1
            return count
        ans = 0
        for i in range(num1, num2 + 1):
            ans +=  (total(i))
        print(ans)
        return ans 
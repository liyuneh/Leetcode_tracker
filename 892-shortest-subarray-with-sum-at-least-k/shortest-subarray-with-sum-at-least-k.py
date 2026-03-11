class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque()
        ans = float("inf")
        total = 0
        for i , n in enumerate(nums):
            if n < 0:
                if q and total + n > 0:
                    # q.append([n, i])
                    total += n
                    while q and q[-1][0] + n < 0:
                        n += (q.pop()[0])
                    if q:
                        q[-1][0] += n

                else:
                    total = 0
                    q.clear()
            else:
                total += n
                q.append([n, i])
                

            while q and total >= k:
                # print(total, i, ans, q)
                ans = min(ans, i - q[0][1] + 1)
                total -= q.popleft()[0]
            # print(q, total)

        return ans if ans != float("inf") else - 1
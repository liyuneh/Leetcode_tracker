class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = deque()
        mn = deque()
        ans = 0
        for i , n in enumerate(nums):
            while mx and abs(mx[0][0] - n ) > limit:
                mx.popleft()
            while mn and abs(mn[0][0] - n ) > limit:
                mn.popleft()
            mxx, mnn = i, i
            while mx and mx[-1][0] < n:
                mxx = mx.pop()[1]
            while mn and mn[-1][0] > n:
                mnn = mn.pop()[1]
            mx.append((n,mxx))
            mn.append((n,mnn))
            ans = max(ans, min(i-mx[0][1], i-mn[0][1]) + 1)
        return ans 
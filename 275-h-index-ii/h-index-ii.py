class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        mx = 0
        n = len(citations)

        l , r = 0, n 
        while l <= r:
            mid = l + ( r - l ) // 2
            x = bisect_left(citations, mid)

            count = n - x
            if count >= mid:
                l = mid + 1
            else:
                r = mid - 1
        return r
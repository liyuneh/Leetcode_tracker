class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)

        while k:
            x = -heapq.heappop(piles)
            x -= x // 2

            heapq.heappush(piles, -x)
            k -= 1
        return -sum(piles)

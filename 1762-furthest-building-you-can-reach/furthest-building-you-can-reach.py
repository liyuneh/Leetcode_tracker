class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ans = []
        for i in range(len(heights) - 1):
            ans.append(max(0, heights[i+1] - heights[i]))
        heap = []
        a = len(heights) - 1
        for i in range(len(ans)):
            if ans[i] > 0:
                heapq.heappush(heap, ans[i])
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                a = i
                break
        
        return a 
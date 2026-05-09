class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap, matrix[i][j])
        while k > 1:
            heapq.heappop(heap)
            k -= 1
        print(heap[0])
        return heap[0]
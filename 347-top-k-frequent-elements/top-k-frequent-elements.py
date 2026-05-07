class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        nums.sort()

        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                heapq.heappush(heap, (cnt, nums[i-1]))

                if len(heap) > k:
                    heapq.heappop(heap)
                cnt = 1
        heapq.heappush(heap, (cnt, nums[-1]))
        if len(heap) > k:
            heapq.heappop(heap)
        
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans
class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        nums.sort()
        freq = defaultdict(int)
        heap = defaultdict(list)
        for c in nums:
            freq[c %space] += 1
            heapq.heappush(heap[c % space],c)
        
        ans = float('inf')
        x = max(freq.values())
        for key, val in freq.items():
            if val == x:
                ans = min(ans, heap[key][0])
        return  ans

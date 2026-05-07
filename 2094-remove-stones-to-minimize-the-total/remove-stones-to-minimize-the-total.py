class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        def heapify_down(nums, n, i):
            cur , l, r = i, 2 * i + 1, 2 * i + 2
            if l < n and nums[l] > nums[cur]:
                cur = l
            if r < n and nums[r] > nums[cur]:
                cur = r
            if cur != i:
                swap(nums, i, cur)
                heapify_down(nums,len(nums), cur)
        def swap(nums, i , j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def replace(nums, val):
            nums[0] = val
            heapify_down(nums, len(nums), 0)
        for i in range(len(piles) // 2, -1, -1):
            heapify_down(piles, len(piles), i)
        while k > 0:
            replace(piles, piles[0] - piles[0] // 2)
            k -= 1
        # print(sum(piles), piles)
        return sum(piles)

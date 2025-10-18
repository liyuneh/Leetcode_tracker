class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        ans = 0
        for i in range(1,arr[-1]):
            if i not in arr:
                count += 1
            if count == k:
                return i
        if count < k:
            count = arr[-1] + (k - count) 
        return count
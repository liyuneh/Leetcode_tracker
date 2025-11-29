class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = sum(nums)
        # if total % k == 0:
        #     return 0
        # if total < k:
        #     return total
        count = 0
        while total % k != 0:
            count += 1
            total -= 1
        return count
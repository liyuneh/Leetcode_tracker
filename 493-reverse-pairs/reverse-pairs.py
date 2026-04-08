class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        def merge(l , r):
            nonlocal count
            if l == r:
                return [nums[l]]
            mid = (r + l) // 2
            left = merge(l, mid)
            right = merge(mid + 1, r)

            for num in left:
                count += bisect_right(right, (num - 1) // 2)
            return sorted(left + right)
        merge( 0, len(nums) - 1)
        return count
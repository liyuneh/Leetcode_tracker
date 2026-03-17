class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums))
        def merge(l, r):
            if l == r:
                return [(nums[l], l)]
            mid = (l + r) // 2
            left = merge(l, mid)
            right = merge(mid + 1, r)
            tmp = [num for num, _ in right]
            
            for num, i in left:
                ans[i] += bisect_left(tmp, num)
            return sorted(left + right)
        merge(0, len(nums) - 1)
        return ans

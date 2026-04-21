class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        if mx - mn == 0:
            return 0
        size = max(1, (mx - mn) // (len(nums) - 1))
        count = (mx - mn) // size + 1
        buck = [[None, None] for _ in range(count)]

        for num in nums:
            now = (num - mn) // size 
            if buck[now][0] is None:
                buck[now][0] = num
                buck[now][1] = num
            else:
                buck[now][0] = min(buck[now][0], num)
                buck[now][1] = max(buck[now][1], num)
        prev = None
        gap = 0
        for a, b in buck:
            if a is None:
                continue
            elif prev is not None:
                gap = max(gap, a - prev)
            prev = b
        
        return gap
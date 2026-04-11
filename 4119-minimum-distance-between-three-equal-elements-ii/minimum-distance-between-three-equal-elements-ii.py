class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq = defaultdict(list)
        for i in range(len(nums)):
            freq[nums[i]].append(i)
        ans = defaultdict(list)
        for key , val in freq.items():
            if len(val ) >= 3:
                ans[key] = val

        mx = max(len(val) for val in freq.values())
        if mx < 3:
            return - 1
        mx = float("inf")
        for key , val in ans.items():
            mn = float("inf")
            for i in range(len(val) - 2):
                x = abs(val[i] - val[i+1]) + abs(val[i] - val[i+2]) + abs(val[i+1] - val[i+2])
                mn = min(mn , x)
            mx = min(mx, mn)
        return mx
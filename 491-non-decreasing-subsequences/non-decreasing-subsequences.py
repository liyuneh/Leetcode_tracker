class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            if sorted(path) == path and len(path) >= 2:
                res.append(path[:])
            
            if start >= len(nums):
                return 
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        backtrack(0,[])
        seen = []
        # new = []
        for r in res:
            if r not in seen:
                seen.append(r)
        return seen
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(i, remaining):
            if remaining == 0:
                res.append(path[:])
                return 
            if remaining < 0:
                return
            for i in range(i, len(candidates)):
                path.append(candidates[i])
                backtrack(i,remaining - candidates[i])
                path.pop()
        backtrack(0, target)
      

        return res
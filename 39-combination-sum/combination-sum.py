class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack():
            if sum(path) == target:
                res.append(path[:])
                return 
            if sum(path) > target:
                return
            for i in range(len(candidates)):
                path.append(candidates[i])
                backtrack()
                path.pop()
        backtrack()
        seen = []
        new = []
        for i in range(len(res)):
            if sorted(res[i]) not in seen:
                new.append(res[i])
                seen.append(sorted(res[i]))

        return new
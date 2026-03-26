class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res  = []
        # ans = [i + 1 for  i in range(k + 1)]
        # print(ans)
        path = []
        def backtrack(start, remaining):
            if len(path) == k and remaining == 0:
                res.append(path[:])
                return 
            if remaining < 0 or len(path) > k:
                return 
            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, remaining - i)
                path.pop()
        backtrack(1,n)

        return res
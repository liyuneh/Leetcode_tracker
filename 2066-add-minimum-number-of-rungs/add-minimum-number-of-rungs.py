class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs = [0] + rungs
        ans = []
        for i in range(1, len(rungs)):
            ans.append(rungs[i] - rungs[i-1])
        count = 0
        for i in range(len(ans)):
            if ans[i] > dist:
                ans[i] -= dist
                count += math.ceil(ans[i] / dist)
        print(count)
        return count
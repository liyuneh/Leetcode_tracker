class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ans = []
        total = 0
        for l , r in costs:
            ans.append([l-r,l,r])
        ans.sort(key=lambda x:x[0])
        for i in range(len(costs) // 2):
            total += ans[i][1]
        for i in range(len(costs) // 2 , len(costs)):
            total += ans[i][2]
        # print(total)
        return total 
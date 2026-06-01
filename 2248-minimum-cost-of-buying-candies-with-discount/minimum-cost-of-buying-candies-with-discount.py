class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse= True)
        ans = 0
        count = 0
        for i in range(len(cost)):
            if count != 2:
                count += 1
                ans += cost[i]
            else:
                count = 0
        print(ans)
        return ans 

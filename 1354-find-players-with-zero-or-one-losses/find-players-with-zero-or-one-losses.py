class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = {}
        ans = []
        seen = set()
        for winner, loser in matches:
            if winner not in seen:
                ans.append(winner)
                seen.add(winner)
            if loser not in seen:
                seen.add(loser)
                ans.append(loser)
            losers[loser] = losers.get(loser, 0) + 1
        ans.sort()
        ans3 , ans2, ans1 = [], [], []
        for i in range(len(ans)):
            if losers.get(ans[i], 0) == 0:
                ans1.append(ans[i])
            elif losers.get(ans[i], 0) == 1:
                ans2.append(ans[i])
        ans3.append(ans1)
        ans3.append(ans2)
        return ans3
            

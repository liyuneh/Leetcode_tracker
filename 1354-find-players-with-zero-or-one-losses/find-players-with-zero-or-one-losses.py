class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = {}
        winners = {}
        for winner, loser in matches:
            winners[winner] = winners.get(winner, 0) + 1
            losers[loser] = losers.get(loser, 0) + 1
        ans1 , ans2 = [], []
        ans3 = []
        for key , values in winners.items():
            if losers.get(key, 0) == 0:
                ans1.append(key)
        ans3.append(sorted(ans1))
        for key , values in losers.items():
            if losers.get(key, 0) == 1:
                ans2.append(key)
        ans2.sort()
        ans3.append(ans2)
        return ans3
            

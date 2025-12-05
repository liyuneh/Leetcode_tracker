class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        count = 0
        for i in range(len(tickets)):
            if i <= k:
                count += min(tickets[i], target)
            else:
                count += min(tickets[i], target - 1)
        
        return count
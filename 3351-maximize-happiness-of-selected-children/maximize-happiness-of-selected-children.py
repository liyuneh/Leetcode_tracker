class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse= True)
        count = 0
        for i in range(k):
            happy = happiness[i] - i
            if happy <= 0:
                break
            count += happy
        return count
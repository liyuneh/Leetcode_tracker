class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = sorted(Counter(nums).items(), key=lambda x:-x[1])
        ans = []
        for i in range(k):
            ans.append(counter[i][0])
        return ans
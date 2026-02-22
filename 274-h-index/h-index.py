class Solution:
    def hIndex(self, citations: List[int]) -> int:
        buckets = [0] * (len(citations) + 1)
        for cite in citations:
            buckets[min(cite, len(citations))] += 1
        cum = 0
        for i in range(len(citations) , - 1, - 1):
            cum += buckets[i]
            if cum >= i:
                return i
    
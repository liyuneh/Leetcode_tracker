class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        table = defaultdict(int)
        for ch in words:
            table[ch] += 1
        sort_t = sorted(table.items(), key=lambda x:(-x[1], x[0]))
        ans = []
        for i in range(k):
            ans.append(sort_t[i][0])
        return ans
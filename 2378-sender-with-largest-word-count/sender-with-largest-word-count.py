class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        freq = defaultdict(int)
        for i,c in enumerate(senders):
            key = messages[i]
            key = key.split()
            for a in key:
                freq[c] += 1
        mx = 0
        for val in freq.values():
            if mx < val:
                mx = val
        ans = []
        for key,val in freq.items():
            if val == mx:
                ans.append(key)
        ans.sort(reverse = True)
        # print(ans[0])
        return ans[0]
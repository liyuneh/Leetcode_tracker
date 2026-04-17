class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        freq = defaultdict(list)
        mn = float("inf")
        for i, ch in enumerate(nums[::-1]):
            x = int(str(ch)[::-1])
            if x in freq:
                val = freq[x][-1]
                mn = min(mn , i - val)
            freq[ch].append(i)
        return mn if mn != float("inf") else -1
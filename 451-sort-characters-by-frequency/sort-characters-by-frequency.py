class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        ans = "".join(sorted(s, key= lambda x:(-counter[x], -ord(x))))
        return ans
class Solution:
    def frequencySort(self, s: str) -> str:
        table = defaultdict(int)

        for char in s:
            table[char] += 1
        sort_s = sorted(table.keys(), key = lambda x : -table[x] )
        ans = "".join(char* table[char]  for char in sort_s)
        return ans
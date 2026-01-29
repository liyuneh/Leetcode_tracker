class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for ch in strs:
            arr = sorted(ch)
            table[tuple(arr)].append(ch)
        return list(table.values())
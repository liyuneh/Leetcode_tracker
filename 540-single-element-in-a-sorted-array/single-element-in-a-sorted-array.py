class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        table = defaultdict(int)
        for c in nums:
            table[c] += 1
        print(table)
        for key , values in table.items():
            if values == 1:
                return key
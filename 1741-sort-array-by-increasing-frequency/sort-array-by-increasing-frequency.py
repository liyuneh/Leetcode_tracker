class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        table = defaultdict(int)
        for num in nums:
            table [num ] += 1
        ans = sorted(nums, key= lambda x: (table[x], -x))
        return ans
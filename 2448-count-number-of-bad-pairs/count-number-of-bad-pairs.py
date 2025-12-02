class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        table = defaultdict(int)
        for i in range(n):
            s = nums[i] - i
            table [s] += 1
        count = 0
        total_pairs = (n * (n - 1)) // 2
        for key, val in table.items():
            count += (val *(val - 1) // 2)
        return total_pairs - count
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        seen = set(nums)

        for x in nums:
            if x + diff in seen and x + 2 * diff in seen:
                count += 1
        return count
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for key, f in counter.items():
            if f > 2:
                return False
        return True
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for c in nums:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        for key , value in dict.items():
            if value >= 2:
                return True
        return False
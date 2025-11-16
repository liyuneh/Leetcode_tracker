class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0
        for num in seen:
            if num - 1 not in seen:
                length = 1
                next_num = num + 1
                while next_num in seen:
                    length += 1
                    next_num += 1
                max_len = max(max_len, length)
        return max_len
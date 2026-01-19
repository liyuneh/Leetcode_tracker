class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_index = {0: -1}
        prefix_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1

            if prefix_sum in prefix_index:
                max_len = max(max_len, i - prefix_index[prefix_sum])
            else:
                prefix_index[prefix_sum] = i

        return max_len

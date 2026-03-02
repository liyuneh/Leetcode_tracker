class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(nums, k):
            c = Counter()
            l = 0
            ans = 0
            for i in range(len(nums)):
                c[nums[i]] += 1
                while len(c) > k:
                    c[nums[l]] -= 1
                    if not c[nums[l]]:
                        del c[nums[l]]
                    l += 1
                ans += (i - l + 1)
            return ans
        return atmost(nums, k) - (atmost(nums, k - 1))
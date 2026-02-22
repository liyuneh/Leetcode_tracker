class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        mn = 0
        j = 0
        while j < len(nums):
            odd , even = 0  , 0 
            seenodd , seeneven = set(), set()
            for i in range(j , len(nums)):
                if nums[i] % 2 == 0 and nums[i] not in seeneven:
                    seeneven.add(nums[i])
                    even += 1
                elif nums[i] % 2 == 1 and nums[i] not in seenodd:
                    seenodd.add(nums[i])
                    odd += 1
                
                if even == odd:
                    mn = max(mn , i - j +  1)
            j += 1
        print(mn)
        return mn

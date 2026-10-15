class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        count = []
        for i in range(len(nums)):
            seen = set()
            seen.add(nums[i])
            ans = 0
            ans += 1
            for j in range(i , len(nums)):
                if nums[i] != nums[j] and nums[j] not in seen:
                    ans += 1
                    seen.add(nums[j])
                count.append(ans)
        ans = sum(x ** 2 for x in count)
        print(ans)
        return ans
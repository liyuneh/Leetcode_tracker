class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        mx = sum(nums[i] for i in range(len(nums)) if nums[i] % 2 == 0)
        ans = []
        for val, index in queries:
            if nums[index] % 2 == 0 and (nums[index] + val) % 2 == 0:
                nums[index] = nums[index] + val
                mx += val
            elif nums[index] % 2 == 1 and (nums[index] + val) % 2 == 0:
                mx += (nums[index] + val)
                nums[index] = nums[index] + val
                print(nums[index])
            elif nums[index] % 2 == 0 and (nums[index] + val) % 2 == 1:
                mx -= nums[index]
                nums[index] = nums[index] + val
            else:
                nums[index] = nums[index] + val
            ans.append(mx)
        return ans
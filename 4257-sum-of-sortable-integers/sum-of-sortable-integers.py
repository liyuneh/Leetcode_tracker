max = 10 ** 5 + 1
ans = {n: [1,n] for n in range(1, max)}
ans[1] = [1]
for i in range(2, max):
    for j in range(i * 2, max , i):
        ans[j].append(i)
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        def valid(d):
            prev = 0
            for i in range(d, n + 1, d):
                desc = -1
                for j in range(i - d, i - 1):
                    if nums[j] > nums[j + 1]:
                        if desc != -1 : return False
                        else: desc = j + 1
                if desc != -1:
                    if nums[i - 1] > nums[i - d] : return False
                    mn, mx = nums[desc], nums[desc - 1]
                else: mn , mx = nums[i-d], nums[i - 1]

                if mn < prev : return False
                prev = mx
            return True
        
        count = 0
        for d in ans[n]:
            if valid(d): count += d
        print(count)
        return count
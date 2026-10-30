class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        pref = list(accumulate(nums))
        print(pref)
        cnt = 0
        for i in range(len(nums)):
            count = nums[i]
            
            cn = str(count)
            if int(cn[0]) == int(cn[-1]) == x:
                cnt += 1

            for j in range(i + 1, len(nums)):
                count += nums[j]
                cn = str(count)
                if int(cn[0]) == int(cn[-1]) == x:
                    cnt += 1
        # print(cnt)
            
        return cnt
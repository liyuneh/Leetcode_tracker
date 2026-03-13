class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        opt = 1
        ans = [[nums[0], 0]]
        prev = 0
        for i in range(1,len(nums)):
            if not ans:
                return opt
            if ans[-1][0] >= (len(nums)- 1 - ans[-1][1] ):
                return opt
            else:
                mx = ans[-1][0]
                b = ans[-1][1]
                x, y = ans.pop()
                prev = -1
                for j in range(y  + 1, (x + y) + 1):
                    if nums[j] + j > mx + b:
                        mx = nums[j]
                        b = j
                if mx and b:
                    print(mx,b)
                    ans.append([mx,b])
                    opt += 1
        return 
            
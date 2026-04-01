class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        res = []
        # def valid(nums):
        #     for i in range(1, len(nums) - 1):
        #         if nums[i+1] - nums[i] != nums[i-1]:
        #             return False
        #     return True
        # path = []

        def backtrack(start):
            if start >= len(num):
                if len(res) <= 2:
                    return False
                for i in range(1, len(res) - 1):
                    if res[i+1] - res[i] != res[i-1]:
                        return False
                return True
            
            if num[start] == '0':
                res.append(0)
                if (backtrack(start + 1)):
                    return True
                res.pop()
                return False
            for i in range(start, len(num)):
                valid = int(num[start:i + 1])
                if len(res) < 2 or int(valid) == res[-1] + res[-2]:
                    res.append(valid)
                    if backtrack(i + 1):
                        return True
                    res.pop()
            return False
        return backtrack(0)
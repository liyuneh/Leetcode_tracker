class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        mn = num
        for i in range(len(nums)):
            flag = False
            prev = -1
            b = 0
            for j in range(i + 1, len(nums)):
                if int(nums[i]) < int(nums[j])  and b <= int(nums[j]):
                    prev = j
                    b = max(b , int(nums[j]))
                    flag = True
            if flag :
                nums[i], nums[prev] = nums[prev], nums[i]
                x = int("".join(nums))
                mn = max(mn , x)
                nums[i], nums[prev] = nums[prev], nums[i]
        print(mn)

        return mn
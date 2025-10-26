class Solution:
    def isBalanced(self, num: str) -> bool:
        odd, even = 0, 0
        for i in range(len(num)):
            if i % 2 == 1 :
                odd += int(num[i])
            else:
                even += int(num[i])
        return odd == even
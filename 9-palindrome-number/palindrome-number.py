class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        k= str(x)
        return k==k[::-1]
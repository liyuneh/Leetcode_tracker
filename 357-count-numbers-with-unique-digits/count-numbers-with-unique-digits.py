class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        ans = 10
        have = 9
        count = 9

        def back(n):
            nonlocal ans,have,count

            if n == 1:
                return 
            
            count *= have
            ans += count
            have -= 1

            back(n -1)
        back(n)
        return ans
            
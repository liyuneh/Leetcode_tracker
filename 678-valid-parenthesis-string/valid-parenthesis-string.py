class Solution:
    def checkValidString(self, s: str) -> bool:


        def backtrack(i, open_count):
            if open_count < 0:
                return False
            if i == len(s):
                return open_count == 0
            if (i, open_count) in memo:
                return memo[(i, open_count)]
            
            if s[i] == "(":
                res = backtrack(i + 1, open_count + 1)
            elif s[i] == ")":
                res = backtrack(i + 1, open_count - 1)
            else:
                if backtrack(i + 1, open_count + 1):
                    res =  True
                elif backtrack(i + 1, open_count - 1):
                    res  = True
                else: 
                    res = backtrack(i + 1, open_count)
            memo[(i , open_count)] = res

            return res
        memo = {}
        return backtrack(0 , 0)
        
            
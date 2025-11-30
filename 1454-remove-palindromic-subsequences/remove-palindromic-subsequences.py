class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(s:str) ->bool:
            return s == s[::-1]
        if is_palindrome(s):
            return 1
        else:
            return 2
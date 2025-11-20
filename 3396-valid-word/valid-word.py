class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        has_vow = False
        has_dig = False
        has_alpha = False

        for ch in word:
            if not ch.isalnum():
                return False
            
            if ch.isdigit():
                has_dig = True
            else:
                if ch.lower() in "aeiou":
                    has_vow = True
                else:
                    has_alpha = True
        return (has_vow  and has_alpha)  or (has_vow  and has_dig and has_alpha)
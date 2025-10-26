class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'AEIOUaeiou'
        s = list(s)
        sorted_vow = sorted([c for c in s if c in vowels])
        l = 0
        for r in range(len(s)):
            if s[r]  in vowels:
                s[r] = sorted_vow[l]
                l += 1
        return ''.join(s)
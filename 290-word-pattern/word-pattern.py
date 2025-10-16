class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(pattern ) != len(word):
            return False
        char = {}
        words = {}

        for c , w in zip(pattern, word):
            if c in char:
                if char[c] != w:
                    return False
            else:
                char[c] = w
            if  w in words:
                if words[w] != c:
                    return False
            else:
                words[w] = c
        return True

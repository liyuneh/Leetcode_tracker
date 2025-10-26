class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1 ) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        count1 = [word1.count(c) for c in set(word1)]
        count2 = [word2.count(c) for c in set(word2)]
        return sorted(count1) == sorted(count2)
        
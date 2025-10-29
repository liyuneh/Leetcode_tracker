class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(ransomNote)
        counter2 = Counter(magazine)
        for key , value in counter.items():
            if counter2[key] < value:
                return False
        return True
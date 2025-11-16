class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        l = 0
        for r in range(len(s2) - len(s1) + 1):
            if Counter(s2[r : r + len(s1)]) == counter:
                return True
        return False
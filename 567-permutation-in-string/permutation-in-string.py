class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        l = 0
        for r in range(len(s2)):
            if r - l + 1 == len(s1):
                if counter == Counter(s2[l:r + 1]):
                    return True
                l += 1
        return False
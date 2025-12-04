class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        for c in t:
            count[c] = count.get(c, 0) + 1
        
        for c in s:
            count[c] -= 1
            if count[c] == 0:
                del count[c]
        k = ""
        for key , val in count.items():
            k += key
        return k
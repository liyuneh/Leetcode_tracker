class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s = sorted(letters)
        if ord(target) >= ord(s[-1]):
            return s[0]
        for i in range(len(s)):
            if ord(s[i]) > ord(target):
                return s[i]
    
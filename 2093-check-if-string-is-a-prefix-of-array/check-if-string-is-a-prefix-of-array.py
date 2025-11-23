class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        k = ""
        for w in words:
            k += w
            if k == s:
                return True
            if len(k) > len(s):
                return False
        return False
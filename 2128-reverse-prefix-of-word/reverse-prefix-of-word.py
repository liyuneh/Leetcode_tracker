class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        x = word.index(ch) if ch in word else 0
        ans = word[0:x+1][::-1] + word[x+1:]
        return ans
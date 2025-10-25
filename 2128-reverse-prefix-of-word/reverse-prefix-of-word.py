class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        for i in range(len(word)):
            if word[i] != ch:
                ans += word[i]
            else:
                ans += word[i]
                break
        words = ans[::-1] + word[len(ans):]
        return words if ch in word else word
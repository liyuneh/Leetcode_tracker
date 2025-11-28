class Solution:
    def replaceDigits(self, s: str) -> str:
        pref = ""
        for i in range(len(s)):
            if s[i].isdigit():
                pref += chr((ord(s[i-1]) - ord('a') + (int(s[i]) % 26)) % 26 + ord('a'))

            else:
                pref += s[i]
        return pref
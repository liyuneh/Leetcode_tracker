class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "").lower()
        unique = []
        seen = set()
        for ch in key:
            if ch not in seen:
                unique.append(ch)
                seen.add(ch)
        map = {}
        for i , ch in enumerate(unique):
            map[ch] = chr(ord('a') + i)
        s = ""
        for ch in message:
            if ch.isalpha():
                s += map[ch]
            else:
                s += " "
        return s
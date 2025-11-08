class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(" ", "")
        sub = [ch for ch in key.lower()]
        unique = []
        seen = set()
        for ch in sub:
            if ch not in seen:
                unique.append(ch)
                seen.add(ch)
        mapp = {ch: chr(97 + i) for i, ch in enumerate(unique)}
        s = ""
        for i in range(len(message)):
            if message[i].isalpha():
                s += mapp[message[i]]
            else:
                s += " "
        return s
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        low, up = [],[]
        lows, upw = set(), set()
        for ch in word:
            if ch.lower() == ch and ch not in lows:
                low.append(ch)
                lows.add(ch)
            elif ch.upper() == ch and ch not in upw:
                up.append(ch)
                upw.add(ch)

        for i in range(len(up)):
            up[i] = up[i].lower()
        ups = set(up)
        count = 0
        for i in range(len(low)):
            if low[i] in ups:
                count += 1
        return count
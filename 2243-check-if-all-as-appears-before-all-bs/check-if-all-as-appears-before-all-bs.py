class Solution:
    def checkString(self, s: str) -> bool:
        a = s.count ('a')
        count = 0
        for ch in s:
            if ch == 'a':
                count += 1
            else:
                break
        if count == a:
            return True
        return False
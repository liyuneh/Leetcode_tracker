class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        ans = [ord(c) - ord('a') for c in s]
        new = [0] * (n + 1 )
        for l , r , dxn in shifts:
            if dxn == 0:
                new[l] -= 1
                new[r + 1 ] += 1 
            else:
                new[l] += 1
                new[r + 1] -= 1 
        pref = 0
        prefs = [0] * n
        for i  in range(len(new) - 1):
            pref += new[i]
            prefs[i] = pref
        for i in range(len(ans)):
            ans[i] += prefs[i]
        for i in range(len(ans)):
            ans[i] = (ans[i] + 26) % 26
        for i in range(len(ans)):
            ans[i] = chr(97 + ans[i])
        return "".join(ans)
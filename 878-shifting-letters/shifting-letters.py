class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        pref = [0] * len(s)
        pref_sum = 0
        shifts.reverse()
        for n in range(len(shifts)):
            pref_sum += shifts[n]
            pref[n] = pref_sum
        pref.reverse()
        ans = []
        for i in range(len(s)):
            shift = pref[i]  % 26
            newchar = chr((ord(s[i]) - ord('a') + shift) % 26+ ord('a'))
            ans.append(newchar)
        return "".join(ans)
class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        n , m = len(s), len(t)
        if n > m:
            return False

        i = j = 0
        left = [-1] * n
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                left[i] = j
                i += 1
            j += 1
        if i == n:
            return True
        
        i, j = n - 1, m - 1
        right = [-1] * n
        while i >= 0 and j >= 0:
            if s[i] == t[j]:
                right[i] = j
                i -= 1
            j -= 1

        for k in range(n):
            pref = k == 0 or left[k - 1] != -1
            suf = k == n - 1 or right[k + 1] != -1

            if not (pref and suf):
                continue
            cnt = - 1 if k == 0 else left[k - 1]
            after = m if k == n - 1 else right [k + 1]

            if cnt + 1 < after:
                return True
        return False
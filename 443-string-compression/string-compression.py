class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        l , r = 0, 1
        cnt = 1
        while r < len(chars):
            if chars[l] == chars[r]:
                cnt += 1
            else:
                s += chars[l]
                if cnt >= 2:
                    s += str(cnt)
                cnt = 1
                l = r
            r += 1
        s += chars[l]
        if cnt >= 2:
            s += str(cnt)
        chars[:] = s
        return len(chars)

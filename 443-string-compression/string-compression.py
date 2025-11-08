class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        count = 1
        l , r = 0, 1
        while r < len(chars):
            if chars[r] == chars[l]:
                count += 1
            else:
                s += chars[l]
                if count >= 2:
                    s += str(count)
                count = 1
                l = r
            r += 1

        s += chars[l]
        if count >= 2:
            s += str(count)
        chars[:] = s

        return len(chars)
        
        print(s)
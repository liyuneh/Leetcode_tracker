class Solution:
    def passwordStrength(self, password: str) -> int:
        spec = "!@#$"
        low = "abcdefghijklmnopqrstuvwxyz"
        cap = low.upper()
        number = "0123456789"
        freq = {}
        for ch in password:
            freq[ch] = 1
        count = 0
        for key in freq:
            if key in spec:
                count += 5
            elif key in low:
                count += 1
            elif key in number:
                count += 3
            elif key in cap:
                count += 2
        return count
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(s):
            parts = s.split(".")
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                if not 0 <= int(part) <= 255:
                    return False
                if part.startswith('0') and len(part) > 1:
                    return False
            return True

        def isIPv6(s):
            parts = s.split(":")
            if len(parts) != 8:
                return False
            for part in parts:
                if len(part) == 0 or len(part) > 4:
                    return False
                try:
                    int(part, 16)
                except ValueError:
                    return False
            return True

        if '.' in queryIP:
            return "IPv4" if isIPv4(queryIP) else "Neither"
        elif ':' in queryIP:
            return "IPv6" if isIPv6(queryIP) else "Neither"
        else:
            return "Neither"

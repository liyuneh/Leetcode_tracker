class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        m = float('-inf')
        for i in range(len(s)):
            
            if  s[i].isdigit():
                if int(s[i]) > m:
                    m = int(s[i])
                    print(m)
                else:
                    return False
        return True
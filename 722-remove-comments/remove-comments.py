class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        m = False
        temp = ""
        for s in source:
            i = 0
            while i < len(s):
                if s[i: i+2] == "/*" and m == False:
                    m = True
                    i += 2
                elif s[i: i+2] == "*/" and m == True:
                    m = False
                    i += 2
                elif s[i: i+2] == "//" and m == False:
                    break
                else:
                    if not m:
                        temp += s[i]
                    i += 1
            if temp and not m:
                res.append(temp)
                temp = ""
        return res

            
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        freq = {}
        for i , ch in knowledge:
            freq[i] = ch
        ans = []
        i = 0
        while i < len(s):
            if s[i] != "(":
                ans.append(s[i])
                i += 1
            else:
                j = i + 1
                temp = []
                while s[j] != ")":
                    temp.append(s[j])
                    j += 1
                x = "".join(temp)
                if x in freq:
                    ans.append(freq[x])
                else:
                    ans.append("?")
                i = j + 1
        print(ans)
            
        return "".join(ans)
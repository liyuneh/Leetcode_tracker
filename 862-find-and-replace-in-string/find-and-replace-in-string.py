class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = []
        i = 0
        while i < len(s):
            found = False
            for j in range(len(sources)):
                if i == indices[j] and s.startswith(sources[j],i):
                    ans.append(targets[j])
                    i += len(sources[j])
                    found = True
                    break
            if not found:
                ans.append(s[i])
                i += 1
        return "".join(ans)
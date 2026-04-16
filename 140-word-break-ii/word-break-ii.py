class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        n = len(s)
        def backtrack(idx, path):
            if idx >= len(s):
                res.append(" ".join(path))
                return 
            for i  in range(len(wordDict)):
                if s[idx:].startswith(wordDict[i]):
                    path.append(wordDict[i])
                    backtrack(idx + len(wordDict[i]), path)
                    path.pop()
        backtrack(0, [])
        return res
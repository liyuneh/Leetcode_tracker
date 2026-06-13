class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for i in range(len(words)):
            count = 0
            for j in range(len(words[i])):
                count += weights[ord(words[i][j]) - ord("a")]
            ans.append(count % 26)
        new = []
        for i in range(len(ans)):
            x = chr(97 + 25 - ans[i])
            new.append(x)
        return "".join(new)
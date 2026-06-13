class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for i in range(len(words)):
            count = 0
            for j in range(len(words[i])):
                count += weights[ord(words[i][j]) - ord("a")]
            ans.append(chr(97 + 25 - count % 26))
        return "".join(ans)
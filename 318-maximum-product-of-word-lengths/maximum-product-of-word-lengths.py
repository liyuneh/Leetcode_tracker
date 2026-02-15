class Solution:
    def maxProduct(self, words: List[str]) -> int:
        freq = {word: set(word) for word in words}
        mx = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if freq[words[i]].isdisjoint(freq[words[j]]):
                    mx = max(mx, len(words[i]) * len(words[j]))

        return mx

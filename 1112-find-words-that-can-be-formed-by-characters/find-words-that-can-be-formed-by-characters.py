class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        ans = 0
        for i in range(len(words)):
            cnt = Counter(words[i])
            found = False
            for j in range(len(words[i])):
                if cnt[words[i][j]] > counter[words[i][j]]:
                    found = True
                    break
            if found:
                ans += 0
            else:
                ans += len(words[i])
        return ans
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        for c in words:
            if ans and Counter(ans[-1]) == Counter(c):
                continue
            elif ans and Counter(ans[-1]) != Counter(c):
                ans.append(c)
        return ans
        
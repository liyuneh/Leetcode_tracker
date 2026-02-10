class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        freq = defaultdict(int)

        changed.sort()
        for ch in changed:
            freq[ch] += 1
        # print(freq)
        ans = []
        for i in range(len(changed)):
            if freq[changed[i]] != 0 and changed[i] * 2 in freq :
                freq[changed[i]] -= 1
                if freq[changed[i] * 2] != 0:
                    ans.append(changed[i])
                    freq[changed[i] * 2] -= 1
            # print(freq)
            if len(ans) == len(changed) // 2:
                return ans
        return []
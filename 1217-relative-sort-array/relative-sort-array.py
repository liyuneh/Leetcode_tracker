class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        freq = dict(sorted(freq.items(), key=lambda x:x[0]))
        ans = []
        for i in range(len(arr2)):
            x = freq[arr2[i]]
            freq[arr2[i]] = 0
            for _ in range(x):
                ans.append(arr2[i])
        for key, val in freq.items():
            if val != 0:
                for _ in range(val):
                    ans.append(key)
        print(ans)
        
        return ans
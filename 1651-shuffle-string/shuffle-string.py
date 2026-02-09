class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = []
        freq = {}
        for i in range(len(indices)):
            freq [indices[i]] = s[i]
        nums = sorted(freq.items(), key=lambda x:x[0])
        print(nums)
        for key, val in nums:
            ans.append(val)
            
        
        return "".join(ans)
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        pref = ""
        ans = []
        for num in nums:
            pref += str(num)
            k = int(pref, 2)
            ans.append(k % 5 == 0)
        return ans
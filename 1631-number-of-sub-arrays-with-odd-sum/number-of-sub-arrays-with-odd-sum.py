class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        Sum = 0
        l = 0
        count = 0
        
        par = [1, 0]
        for r in range(len(arr)):
            Sum += arr[r]
            parity = Sum % 2
            count += par[1 - parity] 
            par[parity] += 1 
        return count  % (10 **9 + 7)
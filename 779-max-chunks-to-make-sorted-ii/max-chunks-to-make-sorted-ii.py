class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx =0
        tr =[0] + [mx:=max(mx, arr[i]) for i in range(len(arr))]
        
        count = 0
        stack = []
        for i in range(len(arr) - 1, - 1 , - 1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            stack.append(arr[i])
            if stack[0] >= tr[i]:
                count += 1
        return count
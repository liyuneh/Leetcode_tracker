class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        
        mx = 0
        for i , c in enumerate(heights):
            if not stack:
                stack.append([c,i])
            elif stack:
                mnn = i
                while stack and stack[-1][0] > c:
                    val , ind = stack.pop()
                    mx = max(mx, val * (i - ind))
                    mnn = ind

                stack.append([c,mnn])
        while stack:
            val , ind = stack.pop()
            mx = max(mx, val * (len(heights) - ind ))

        return mx
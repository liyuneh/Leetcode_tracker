class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        stack = []
        for i in range(len(image)):
            image[i].reverse()
            stack.append(image[i])
        prime = []
        for i in range (len(stack)):
            ans = []
            for j in range(len(stack[i])):
                if stack[i][j] == 1:
                    stack[i][j] = 0
                    ans.append(stack[i][j])
                elif stack[i][j] == 0:
                    stack[i][j] = 1
                    ans.append(stack[i][j])
            prime.append(ans)
        return prime
                
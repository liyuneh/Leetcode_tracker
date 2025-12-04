class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for c in asteroids:
            while stack and c < 0 and stack[-1] > 0:
                if abs(c) < stack[-1]:
                    c = 0
                    break
                elif abs(c) > stack[-1]:
                    stack.pop()
                else:
                    stack.pop()
                    c = 0
                    break
            if c :
                stack.append(c)
        return stack
                
            
            
        return stack
                    
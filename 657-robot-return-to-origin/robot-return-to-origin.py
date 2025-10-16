class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move = {
            'L' : -1,
            'R' : 1,
            'U' : 1,
            'D' : -1
        }
        start = [0,0]
        for c in moves:
            if c == "L" or c == "R":
                start[0] += move[c]
            elif c == "U" or c == "D":
                start[1] += move[c]
        return start == [0,0]
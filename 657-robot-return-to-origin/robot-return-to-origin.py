class Solution:
    def judgeCircle(self, moves: str) -> bool:
        countlr , countud = 0,0
        for i in range(len(moves)):
            if moves[i] == "L":
                countlr -= 1
            elif moves[i] == "R":
                countlr += 1
            elif moves[i] == "U":
                countud += 1
            else:
                countud -= 1
        return countlr == countud == 0
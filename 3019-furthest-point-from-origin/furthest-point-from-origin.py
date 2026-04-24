class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        countl = moves.count("L")
        countr = moves.count("R")
        mx , mn = max(countl, countr) , min(countl, countr)
        return len(moves) - 2 * mn
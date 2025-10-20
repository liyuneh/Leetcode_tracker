class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        candidates = {
            "--X": -1,
            "X--" :-1,
            "++X" : 1,
            "X++" : 1
        }
        ans = 0
        for c in operations:
            ans += candidates[c]
        return ans
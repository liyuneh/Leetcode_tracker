class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for ch in hours:
            if ch >= target:
                count += 1
        return count
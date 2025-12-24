class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum (apple)
        capacity.sort(reverse = True)
        i = 0
        count = 0
        while total > 0:
            total -= capacity[i]
            count += 1
            i += 1
        return count
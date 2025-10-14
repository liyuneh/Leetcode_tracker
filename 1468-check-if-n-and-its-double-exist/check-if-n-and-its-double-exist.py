class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        def binarysearch(target, excludeindex):
            left , right = 0, len(arr) - 1
            while left <= right :
                middle = left + (right - left) // 2
                if arr[middle] == target and middle != excludeindex:
                    return True
                elif arr[middle] < target:
                    left  = middle + 1
                else:
                    right = middle - 1
            return False
        for i in range(len(arr)):
            if binarysearch(arr[i] * 2, i):
                return True
        return False
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l , r = 0 ,0
        n , m = len(version1), len(version2)

        while l < n or  r < m:
            num1 = 0
            while l < n and version1[l] != ".":
                num1 += num1 * 10 + int(version1[l])
                l += 1
            l += 1

            num2 = 0 
            while r < m and version2[r] != ".":
                num2 += num2 * 10 + int(version2[r])
                r += 1
            r += 1

            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0
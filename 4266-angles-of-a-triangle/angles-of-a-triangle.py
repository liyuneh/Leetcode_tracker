class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        nums = sorted(sides)
        if nums[0] + nums[1] <= nums[2]:
            return []
        a,b,c = nums
        xa = ((b**2 + c ** 2) - (a ** 2)) / (2 * b * c)
        xb = ((a ** 2 + c ** 2) - (b ** 2)) / (2 * a * c)
        xc = ((b ** 2 + a ** 2) - (c ** 2)) / (2 * b * a)
        # print(xa,xb,xc)
        # angle = math.degrees(math.acos(0))
        a = math.degrees(math.acos(xa))
        b = math.degrees(math.acos(xb))
        c = math.degrees(math.acos(xc))
        return [a,b,c]
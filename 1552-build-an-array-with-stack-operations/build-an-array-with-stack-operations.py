class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        num = 1
        for t in target:
            while num < t:
                res.append("Push")
                res.append("Pop")
                num += 1
            res.append("Push")
            num += 1
        return res

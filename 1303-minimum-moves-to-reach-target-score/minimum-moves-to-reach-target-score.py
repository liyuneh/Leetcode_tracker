class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # if maxDoubles == 0:
        #     return target - 1
        count = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 != 0 :
                target -= 1
            else:
                target = target // 2
                maxDoubles -= 1
            count += 1
        if target:
            count += (target - 1)
        # print(count)
        return count 
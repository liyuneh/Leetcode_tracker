class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def horizental(grid):
            n = len(grid)
            m = len(grid[0])
            hori = []
            for i in range(n):
                hori.append(sum(grid[i]))
            pref1, suff1 = [], []
            pre, suf = 0 , 0
            for i in range(len(hori)):
                pre += hori[i]
                pref1.append(pre)
            for i in range(len(hori)-1, -1 ,- 1):
                suf += hori[i]
                suff1.append(suf)
            suff1.reverse()

            for i in range(len(pref1) - 1):
                if pref1[i] == suff1[i + 1]:
                    return True
            return False


        def vertical(grid):
            ver = [sum(col) for col in zip(*grid)]
            front , back = [], []
            f, b = 0 , 0
            for i in range(len(ver)):
                f += ver[i]
                front.append(f)
            for i in range(len(ver) - 1 ,- 1,- 1):
                b += ver[i]
                back.append(b)
            back.reverse()
            for i in range(len(front) - 1):
                if front[i] == back[i + 1]:
                    return True
            return False
        

        return horizental(grid) or vertical(grid)

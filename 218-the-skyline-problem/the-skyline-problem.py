class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        hulum = []
        for l, r, h in buildings:
            hulum.append((l, h, 1, l))
            hulum.append((r, h, 0, l))
        hulum.sort()
        hp = []
        deleted = set()
        ans = defaultdict(int)
        prev = -1
        for point, h, t, orig in hulum:
            if t:
                heappush(hp, (-h, point))
            elif hp:
                deleted.add((-h, orig))
            while hp and hp[0] in deleted:
                heappop(hp)
            cur = -hp[0][0] if hp else 0
            if cur != prev:
                ans[point] = max(ans[point], cur)
                prev = cur
                
        stack = []
        for point, cur in sorted(ans.items()):
            if not stack or stack[-1][1] != cur:
                stack.append((point, cur))

        return stack
            
            


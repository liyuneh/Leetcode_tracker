class Solution:
    def minOperations(self, nums: List[int]) -> int:
        q = deque()
        opt = 0
        for c in nums:
            if not q:
                if c == 0:
                    q.append(c)
            elif q and len(q) < 3:
                q.append(c)
            if len(q) == 3:

                while q and q[0] == 0:
                    q.popleft()
                for i in range(len(q)):
                    if q[i] == 0:
                        q[i] = 1
                    else:
                        q[i] = 0
                opt += 1
        if len(q) != 0:
            return -1
        return opt
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = [deque(), deque()]
        opt = 0
        un = 0
        flip = 1
        for c in nums:
            # print(q[un])
            # print(q[flip])
            if not q[un]:
                if c == 0:
                    q[un].append(c)
                    q[flip].append(1 ^ c)
            elif q[un] and len(q[un]) < k:
                q[un].append(c)
                q[flip].append(1 ^ c)
            if len(q[un]) == k:
                while q[flip] and q[flip][0] == 1:
                    q[un].popleft()
                    q[flip].popleft()
                un, flip = flip, un
                opt += 1
        if len(q[0]) != 0:
            return -1
        return opt
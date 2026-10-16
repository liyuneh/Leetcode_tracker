Mod = 10 ** 9 + 7
class New:
    def __init__(self, n):
        self.st = [[0, 0, 0] for _ in range(4 * n)]

    def apply(self, node, l, r, val):
        s, sq, lazy = self.st[node]
        length = r - l + 1
        self.st[node][0] = (s + length * val) % Mod
        self.st[node][1] = (sq + 2 * val * s + length * val ** 2) % Mod
        self.st[node][2] = (lazy + val) % Mod

    def update(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return

        if ql <= l and r <= qr:
            self.apply(node, l, r, 1)
            return

        lazy = self.st[node][2]
        mid = (l + r) // 2

        if lazy > 0 and l != r:
            self.apply(node * 2, l, mid, lazy)
            self.apply(node * 2 + 1, mid + 1, r, lazy)
            self.st[node][2] = 0

        self.update(node * 2, l, mid, ql, qr)
        self.update(node * 2 + 1, mid + 1, r, ql, qr)

        left = self.st[node * 2]
        right = self.st[node * 2 + 1]
        self.st[node][0] = (left[0] + right[0]) % Mod
        self.st[node][1] = (left[1] + right[1]) % Mod

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        st = New(n)
        last = {}
        res = 0

        for i, num in enumerate(nums):
            p = last.get(num, -1)
            st.update(1, 0, n - 1, p + 1, i)
            res = (res + st.st[1][1]) % Mod
            last[num] = i

        return res
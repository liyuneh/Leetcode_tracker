class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        freq = defaultdict(int)
        count = 0
        for num in sorted(nums):
            if not groups or abs(num - groups[-1][-1]) > limit:
                groups.append(deque())
                count += 1
            groups[-1].append(num)
            freq[num] = count - 1
        res = []
        for num in nums:
            now = freq[num]
            res.append(groups[now].popleft())
        return res
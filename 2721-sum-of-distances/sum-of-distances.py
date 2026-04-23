class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)

        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = [0] * len(nums)

        for x, arr in pos.items():
            n = len(arr)
            prefix = [0] * (n + 1)

            for i in range(n):
                prefix[i + 1] = prefix[i] + arr[i]

            for i in range(n):
                left = arr[i] * i - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - arr[i] * (n - i - 1)
                ans[arr[i]] = left + right

        return ans
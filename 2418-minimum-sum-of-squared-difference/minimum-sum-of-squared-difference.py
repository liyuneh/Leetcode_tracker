class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:

        ans = [abs(x - y) for x, y in zip(nums1, nums2)]
        k = k1 + k2

        if sum(ans) <= k:
            return 0

        left, right = 0, max(ans)

        while left < right:
            mid = (left + right) // 2
            needed = sum(max(0, x - mid) for x in ans)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        ans = [min(x, left) for x in ans]
        k -= sum(abs(x - y) for x, y in zip(ans, [abs(a - b) for a, b in zip(nums1, nums2)]))

        ans.sort(reverse=True)

        for i in range(len(ans)):
            if k == 0:
                break
            if ans[i] == left and ans[i] > 0:
                ans[i] -= 1
                k -= 1

        return sum(x * x for x in ans)
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        def swap(arr,i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def heapify_down(arr, n, i):
            cur = i
            left ,right = 2 * i + 1, 2 * i + 2
            if left < n and arr[left] > arr[cur]:
                cur = left
            if right < n and arr[right] > arr[cur]:
                cur = right
            if cur != i:
                swap(arr, i, cur)
                heapify_down(arr, n, cur)
        def replace(nums, val):
            nums[0] = val
            heapify_down(nums, len(nums), 0)
        for i in range((len(nums) - 1) // 2, -1, -1):
            heapify_down(nums, len(nums), i)
        total = 0
        while k > 0:
            total += nums[0]
            replace(nums,  math.ceil(nums[0] / 3))
            k -= 1
        return total 
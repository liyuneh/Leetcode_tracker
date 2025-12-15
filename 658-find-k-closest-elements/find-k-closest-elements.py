class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr) 
        def search (nums:List[int], target:int)->int:
            l , r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans 
        index = search(arr, x)
        left = index
        right = index + 1
        ans = []
        while k > 0:
            if left < 0:
                ans.append(arr[right])
                right += 1
            elif right >= n:
                ans.append(arr[left])
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                ans.append(arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1
            k -= 1
        return sorted(ans)
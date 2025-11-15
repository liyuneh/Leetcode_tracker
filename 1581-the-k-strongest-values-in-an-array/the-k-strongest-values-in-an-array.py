class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[(n-1) // 2]
        l , r = 0 , len(arr) - 1
        ans = []
        while l <= r:
            if abs(arr[l] - m) > abs(arr[r] - m):
                ans.append(arr[l])
                l += 1
            else:
                ans.append(arr[r])
                r -= 1
        print(ans)
        return ans[:k]
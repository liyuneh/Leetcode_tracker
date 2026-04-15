class Solution:
    def createSortedArray(self, arr: List[int]) -> int:
        ansl , ansr = [0] * len(arr), [0] * len(arr)
        def merg(l , r):
            nonlocal arr
            if l == r:
                return [[arr[l], l]]
            mid = (l + r) // 2
            left = merg(l, mid)
            right = merg(mid + 1, r)
    
            tmp = [num for num, _ in left]
            tmp1 = [num for num, _ in left]
            for num, i in right:
                ansl[i] += (len(left) - bisect_right(tmp, num))
            for num, i in right:
                ansr[i] += (bisect_left(tmp, num))



            return sorted(left + right)
        merg(0, len(arr) - 1)
        # print(ansl)
        # print(ansr)
        # print()
        count = 0
        for i in range(len(ansl)):
            count += min(ansl[i], ansr[i])
        # print(count)
        # print()
        return (count % (10 ** 9 + 7))
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr == sorted(arr):
            return []
        ans = []
        per = [i for i in range(1, len(arr) + 1)]
        for i in range(len(arr) - 1, - 1, - 1):
            if per[i] != arr[i]:
                x = arr.index(per[i])
                # print(x)
                arr = arr[:x+1][::-1] + arr[x+1:]
                # print(arr)
                ans.append(x + 1)
                arr = arr[:per[i]][::-1]
                # print(arr)
                ans.append(per[i])
        return  ans
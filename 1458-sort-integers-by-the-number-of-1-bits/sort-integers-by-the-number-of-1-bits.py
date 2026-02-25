class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        freq = defaultdict(list)
        arr.sort()
        for i in range(len(arr)):
            x = bin(arr[i])[2:]
            y = x.count("1")
            freq[y].append(arr[i])
        ans = []
        nums = sorted(freq.items() ,key = lambda x:x[0])
        print(nums)
        for x , val in nums:
            ans.extend(sorted(val))
        print(ans)
        return ans
        
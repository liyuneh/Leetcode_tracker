class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        freq = defaultdict(list)
        for i, c in enumerate(nums):
            freq[c].append(i)

        ans = []
        n = len(nums)
        for i in range(len(queries)):
            num = nums[queries[i]]
            a = freq[num]
            if len(a) <= 1:
                ans.append(-1)
            elif a[0] == queries[i]:
                ans.append(min( n - (a[-1] - a[0]), a[1] - a[0]))
            elif a[-1] == queries[i]:
                ans.append(min(a[-1] - a[-2],  n - (a[-1] - a[0])))
               
            else:
                x = bisect_left(a,queries[i])
                y = bisect_right(a,queries[i])
                
                ans.append(min(a[y] - queries[i], queries[i] - a[x - 1]))
        print(ans)   
        return ans
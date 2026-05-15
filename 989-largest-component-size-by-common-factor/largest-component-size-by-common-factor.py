class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        parent = {}
        size = {}
        for x  in nums:
            parent[x] = x
            size[x] = 1
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return parent[x]
        def union(x, y):
            a, b = find(x), find(y)
            if a == b:
                return 
            if size[a] < size[b]:
                a, b = b , a
            parent[b] = a
            size[a] += size[b]
            return True  

        freq = {}
        for num in nums:
            x = num
            start = 2

            while start * start <= x:
                if x % start == 0:
                    if start in freq:
                        union(num, freq[start])
                    else:
                        freq[start] = num 
                    
                    while x % start == 0:
                        x //= start
                start += 1

            if x > 1:
                if x in freq:
                    union(num, freq[x])
                else:
                    freq[x] = num
        ans = 0

        for num in nums:
            ans = max(ans, size[find(num)])
        print(ans)
        
        return ans
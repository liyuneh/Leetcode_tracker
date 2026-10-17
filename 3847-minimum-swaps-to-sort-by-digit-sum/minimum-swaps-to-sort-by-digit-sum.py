class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        now = []
        n = len(nums)

        for i in range(len(nums)):
            x = str(nums[i])
            now.append((sum(int(digit) for digit in x), nums[i]))
        now.sort()
        print(now)
        freq = {}
        for i in range(len(now)):
            freq[now[i][1]] = i
        new = [0] * (n)
        for i in range(len(nums)):
            new[i] = freq[nums[i]]
        
        visited = [False] * n
        swap = 0

        for i in range(n):
            if visited[i] or new[i] == i:
                continue
            j = i 
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = new[j]
                cycle += 1
            swap += (cycle - 1)
        print(swap)
        return swap
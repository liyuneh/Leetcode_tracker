class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def seive(n):
            prime = [True] * (n + 1)
            prime[1] = prime[0] = False

            p = 2
            while p * p <= n:
                if prime[p]:
                    for i in range(p * p, n + 1 , p):
                        prime[i] = False
                p += 1
            res = []
            for i in range(n + 1):
                if prime[i]:
                    res.append(i)
            return res
        # ans = print(seive(2))
        seen = set()
        for i in range(len(nums)):
            ans = seive(nums[i])
            # print(ans)
            for j in range(len(ans)):
                if nums[i] % ans[j] == 0 and ans[j] not in seen:
                    seen.add(ans[j])
        # print(len(seen))
        return len(seen)
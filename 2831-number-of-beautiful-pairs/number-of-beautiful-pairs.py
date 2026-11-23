class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            x = int(str(nums[i])[0])
            for j in range(i + 1, len(nums)):
                if math.gcd(x, nums[j] % 10) == 1:
                    cnt += 1
        # print(cnt)
        return  cnt
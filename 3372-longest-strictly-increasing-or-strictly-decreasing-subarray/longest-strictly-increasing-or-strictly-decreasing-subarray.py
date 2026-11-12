class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1

        # sign = "+" if nums[0] > nums[1] else "-"
        # q = deque()
        # ans = 1
        # for c in nums:
        #     if not q:
        #         q.append(c)
        #     elif len(q) and  sign == "+" and q[-1] < c:
        #         q.append(c)
        #     elif  q and  sign == "+" and q[-1] > c:
        #         ans = max(ans, len(q))
        #         while len(q) > 1:
        #             q.popleft()
        #         sign = "-"
        #         q.append(c)
        #     elif q and sign == "-" and q[-1] < c:
        #         ans = max(ans, len(q))
        #         while len(q) > 1:
        #             q.popleft()
        #         sign = "+"
        #         q.append(c)
        #     elif q and sign == "-" and q[-1] > c:
        #         q.append(c)
        #     else:
        #         ans = max(ans, len(q))
        #         while len(q) > 0:
        #             q.popleft()
        #         q.append(c)
        
        # print(ans)
        ans = 1
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cnt  += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
        # print(ans, cnt)/
        ans = max(ans,cnt)
        cnt1 = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                cnt1 += 1
            else:
                ans = max(ans, cnt1)
                cnt1 = 1
        ans = max(ans, cnt1)
        return ans
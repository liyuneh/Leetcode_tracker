class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        nums = sorted( freq.items(), key = lambda x:x[0])
        ans = []
        x = ""
        for l , r in nums:
            if r % 2 == 0:
                ans.append(r // 2 * l)
            else:
                ans.append(r// 2 * l)
                x = l
        # print("".join(ans) + x + "".join(ans)[::-1])
        return "".join(ans) + x + "".join(ans)[::-1]
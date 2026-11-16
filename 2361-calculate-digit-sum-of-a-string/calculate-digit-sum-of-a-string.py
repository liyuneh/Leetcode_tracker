class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s

        while len(s) > k:
            ans = []
            i = 0
            a = ""
            cnt = 0
            while i < len(s):
                a += s[i]
                cnt += 1
                if cnt == k:
                    ans.append(a)
                    a = ""
                    cnt = 0
                i += 1
            if cnt:
                ans.append(a)
            # print(ans)
            for j in range(len(ans)):
                ans[j] = str(sum(int(x) for x in ans[j]))
            s = "".join(ans)
        # print(s)
        return s
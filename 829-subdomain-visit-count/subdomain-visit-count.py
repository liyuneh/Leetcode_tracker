class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        for i in range(len(cpdomains)):
            x = cpdomains[i].split()
            x1 = x[1].split(".")
            for i in range(len(x1)):
                temp = x[0] + " " + ".".join(x1[i:])
                ans.append(temp)
        # print(ans)
        # print()
        freq = {}
        for i in range(len(ans)):
            x1, x2 = ans[i].split()
            freq[x2] = freq.get(x2, 0) + int(x1)
        ans2 = []
        for key , val in freq.items():
            x = f"{val} {key}"
            ans2.append(x)

            
        return ans2
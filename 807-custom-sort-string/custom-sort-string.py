class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = list(order)
        counter = Counter(s)
        ls = []
        for i in range(len(ans)):
            if ans[i] in counter:
                ls.append(ans[i] * counter[ans[i]])
                counter[ans[i]] = 0
        for key , val in counter.items():
            if val != 0:
                ls.append(key * val)
        
            
        return "".join(ls)
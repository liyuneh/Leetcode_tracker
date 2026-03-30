class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if Counter(s1) != Counter(s2):
            return False
        ans, ans1 = defaultdict(list), defaultdict(list)
        for i , ch in enumerate(s1):
            ans[ch].append(i + 1)
        for i, ch in enumerate(s2):
            ans1[ch].append(i + 1)
        for key, val in ans1.items():
            for i in range(len(val)):
                ans[key].append(val[i])
        for key, val in ans.items():
            counteven, countodd = 0, 0
            for i in range(len(val)):
                if val[i] % 2 == 0:
                    counteven += 1
                else:
                    countodd += 1
            if counteven % 2 != 0 or countodd % 2 != 0:
                return False
        
        return True
        
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for i in range(len(paths)):
            x = paths[i].split()
            for i in range(1, len(x)):
                freq[x[i][x[i].index('(') + 1:-1]].append(x[0]+"/"+x[i][:x[i].index('(')])
        ans = []
        for val in freq.values():
            if len(val) >= 2:
                ans.append(val)
            
        return ans
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        original = [[] for _ in range(n)]

        for i in range(1,n):
            original[parent[i]].append(i)
        new = list(parent)
        seen = [-1] * 26

        def dfs1(node):
            chr_ind = ord(s[node]) - 97
            old = seen[chr_ind]
            seen[chr_ind] = node
            for child in original[node]:
                c_ind = ord(s[child]) - 97
                if seen[c_ind] != -1:
                    new[child] = seen[c_ind]
                dfs1(child)
            seen[chr_ind] = old
        dfs1(0)
        # print(new)

        new_one = [[] for _ in range(n)]
        for i in range(1, n):
            new_one[new[i]].append(i)
        ans = [0] * n
        def dfs2(node):
            size = 1
            for child in new_one[node]:
                size += dfs2(child)
            ans[node] = size
            return size
        
        dfs2(0)
        # print(new_one)

        return ans
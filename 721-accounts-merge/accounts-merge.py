class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            while x != parent[x]:
                x = parent[x]
            return parent[x]
        def union(x, y):
            a , b = find(x), find(y)
            if a != b:
                parent[b] = a
            return True
        parent = list(range(len(accounts)))
        email = {}
        for i , acc in enumerate(accounts):
            name = acc[0]
            for em in acc[1:]:
                if em in email:
                    k = email[em]

                    if accounts[k][0] == name:
                        union(i, k)
                email[em] = i
        g = defaultdict(set)
        for i , acc in enumerate(accounts):
            root = find(i)
            g[root].update(acc[1:])
        res = []
        for root, email in g.items():
            name = accounts[root][0]
            res.append([name] + sorted(email))
        print(res)
        return res
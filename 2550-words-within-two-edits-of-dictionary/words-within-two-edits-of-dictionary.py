class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def diff(s, p):
            count = 0
            for i in range(len(s)):
                if s[i] != p[i]:
                    count += 1
            return count
        ans = []
        for i in range(len(queries)):
            found = False
            for j in range(len(dictionary)):
                if queries[i] == dictionary[j] or diff(queries[i], dictionary[j]) <= 2:
                    found = True
                    break
            if found:
                ans.append(queries[i])
        # print(ans)
        return ans
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ans1 = list(map(int,version1.split(".")))
        ans2 = list(map(int, version2.split('.')))
        max_len = max(len(ans1), len(ans2))

        ans1 += [0] * (max_len - len(ans1))
        ans2 += [0] * (max_len - len(ans2))

        for i in range(max_len):
            if ans1[i] > ans2[i]:
                return 1
            elif ans1[i] < ans2[i]:
                return -1
        return 0
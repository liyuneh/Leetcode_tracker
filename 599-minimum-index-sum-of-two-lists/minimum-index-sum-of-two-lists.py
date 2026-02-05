class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = []
        mn = float('inf')

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j] and mn > i + j:
                    if res:
                        res.pop()
                    res.append(list1[i])
                    mn = i + j
                elif list1[i] == list2[j] and mn == i + j:
                    res.append(list1[i])
                    mn = i + j
        return res
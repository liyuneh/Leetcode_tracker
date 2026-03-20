class Solution:
    def candy(self, ratings: List[int]) -> int:
        ratings = [-1] + ratings
        ans1= []
        count = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                count += 1
                ans1.append(count)
            else:
                count = 1
                ans1.append(count)
        mx = 1
        ans2 = [1]
        for i in range(len(ratings) - 2, 0, -1):
            if ratings[i] > ratings[i+1]:
                mx += 1
                ans2.append(mx)
            else:
                mx = 1
                ans2.append(mx)
        ans2.reverse()
        final = 0
        for i in range(len(ans1)):
            final += (max(ans1[i], ans2[i]))
        return final
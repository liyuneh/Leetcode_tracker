class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        x = min(skill)
        y = max(skill)
        skill.sort()
        ans = 0
        l , r = 0 , len(skill) - 1
        while l < r:
            if skill[l] + skill[r] != x + y:
                return -1
            else:
                ans += (skill[r] * skill[l])
            l += 1
            r -= 1
        print(ans)
        return ans
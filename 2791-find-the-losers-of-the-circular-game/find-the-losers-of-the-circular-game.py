class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = set()
        pos = 0
        count = 1
        while pos not in seen:
            seen.add(pos)
            pos = (pos + count * k) % n
            count += 1
        ans = [i+1  for i in range(n) if i not in seen]
        return ans

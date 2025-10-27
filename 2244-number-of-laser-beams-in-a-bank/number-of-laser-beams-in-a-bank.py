class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        left = 0
        for r in range(1,len(bank)):
            if '1' in bank[left] and '1' in bank[r]:
                countleft = bank[left].count('1')
                countright = bank[r].count('1')
                count += (countleft * countright)
                left = r
            if '1' not in bank[left]:
                left += 1
        return count
            
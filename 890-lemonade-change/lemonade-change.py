class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5:
            return False
        freq = defaultdict(int)
        for ch in bills:
            if ch == 20:
                if freq[10] != 0:
                    freq[10] -= 1
                    if freq[5] :
                        freq[5] -= 1
                    else:
                        return False
                elif freq[5] >= 3:
                    freq[5] -= 3
                else:
                    return False
            elif ch == 10:
                if freq[5]:
                    freq[5] -= 1
                else:
                    return False
            freq[ch] += 1
        return True
        
                
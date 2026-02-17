class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        n = len(s)
        freq = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
        }

        if n == 1:
            return freq[s[0]]
        elif n == 2:
            return [x + y  for x in freq[s[0]] for y in freq[s[1]]]
        elif n == 3:
            return [x + y + z for x in freq[s[0]] for y in freq[s[1]] for z in freq[s[2]]]
        else:
            return [x + y + z + k for x in freq[s[0]] for y in freq[s[1]] for z in freq[s[2]] for k in freq[s[3]]]
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        freq = {}

        for i , n in enumerate(secret):
            freq[i] = n
        bulls = 0
        seen = set()
        for i in range(len(guess)):
            if guess[i] == freq[i]:
                bulls += 1
                seen.add(i)
                del freq[i]
        cows = 0
        for i in range(len(guess)):
            for key , val in freq.items():
                if val == guess[i] and i not in seen:
                    cows += 1
                    freq[key] = "visisted"
                    seen.add(i)

        return f"{bulls}A{cows}B"
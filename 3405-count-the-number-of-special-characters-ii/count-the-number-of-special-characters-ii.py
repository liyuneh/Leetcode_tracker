class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        freq = defaultdict(int)
        for i, ch in enumerate(word):
            if ch.lower() == ch :
                freq[ch] = i
            else:
                if ch not in freq:
                    freq[ch] = i
        count = 0
        for ch in word:
            if ch.upper() == ch:
                if ch.lower() in freq:
                    if freq[ch] > freq[ch.lower()]:
                        count += 1
                        del[freq[ch.lower()]]
                        del freq[ch]
        print(count)
        return count
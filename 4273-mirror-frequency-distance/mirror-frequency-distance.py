class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = defaultdict(int)
        for ch in s:
            freq[ch]  += 1
        for i in range(len(s)):
            if s[i].isdigit():
                x = chr(ord("0") + ord("9") - ord(s[i]))
                if x in freq and freq[x] > 0:
                    freq[s[i]] -= 1
                    freq[x] -= 1
                    if freq[x] == 0:
                        del freq[x]
                    if freq[s[i]] == 0:
                        del freq[s[i]]
            else:
                y = chr(ord("a") + ord("z") - ord(s[i]))
                if y in freq and freq[y] > 0:
                    freq[y] -= 1
                    freq[s[i]] -= 1
                    if freq[y] == 0:
                        del freq[y]
                    if  freq[s[i]] == 0:
                        del freq[s[i]]
        print(freq)
        count = 0
        for key , val in freq.items():
            count += abs(val)

        return count
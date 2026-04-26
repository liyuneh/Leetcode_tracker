class Solution:
    def sortVowels(self, s: str) -> str:
        freq = defaultdict(int)
        for i in range(len(s)):
            if s[i] in "aeiou":
                freq[s[i]] += 1
        nums = sorted(freq.items(), key = lambda x:-x[1])
        ans = deque()
        for x, y in nums:
            for i in range(y):
                ans.append(x)
        s = list(s)
        for i in range(len(s)):
            if s[i] in "aieou":
                s[i] = ans.popleft()
        print("".join(s))
        return "".join(s)
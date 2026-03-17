class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter()
        counter_t = Counter(t)

        i , l = 0 ,0 
        mn = float("inf")
        mn_string = ""
        ans = []
        while i < len(s):
            counter[s[i]] += 1
            while counter >= counter_t:
                if i - l + 1 < mn:
                    mn = i - l + 1
                    mn_string = s[l:i+1]
                counter[s[l]] -= 1
                l += 1
            i += 1
        
        return mn_string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <=1 or k == len(s):
            return len(s)
        
        i, j = 0, 0
        res = 0
        count = {}
        maxFreq = 0

        while j<len(s):
            count[s[j]] = 1 + count.get(s[j], 0)
            maxFreq = max(maxFreq, count[s[j]])

            while j-i+1 - maxFreq > k:
                count[s[i]] -= 1
                i += 1


            res = max(res, j-i+1)
            j += 1
        
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0:
            return len(s)
        
        i, j = 0, 0
        map = {}
        res = 0
        while j < len(s):
            # char
            c = s[j]

            if c in map and map[c] >= i:
                i = map[c] + 1
            
            res = max(res, j-i+1)
            map[c] = j

            # default increment on j
            j +=1
        return res
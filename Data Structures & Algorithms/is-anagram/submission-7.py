class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # map 

        # sMap, tMap = {}, {}

        # for i in range(len(s)):
        #     sMap[s[i]] = 1 + sMap.get(s[i], 0)
        #     tMap[t[i]] = 1 + tMap.get(t[i], 0)
        
        # return sMap == tMap

        # list

        chars = [0] * 26

        for i in range(len(s)):
            chars[ord(s[i]) - ord('a')] += 1
            chars[ord(t[i]) - ord('a')] -= 1
        
        for i in range(26):
            if chars[i] != 0:
                return False
        
        return True
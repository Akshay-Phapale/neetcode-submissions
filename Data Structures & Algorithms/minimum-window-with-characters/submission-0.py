class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window, countT = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        i, j = 0, 0
        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(countT)
        while j < len(s):

            window[s[j]] = 1 + window.get(s[j], 0)

            if s[j] in countT and window.get(s[j]) == countT.get(s[j]):
                have += 1
            
            while have == need:
                window[s[i]] = window.get(s[i]) - 1
                if s[i] in countT and window.get(s[i]) < countT.get(s[i]):
                    have -= 1
                if j - i + 1 < resLen:
                    resLen = j - i + 1
                    res = [i, j]     
                i += 1 

            j += 1
        i, j = res
        return s[i:j+1] if resLen != float("infinity") else ""
        
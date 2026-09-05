class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
            
        
        map = defaultdict(list)

        for s in strs:
            freq = [0] * 26

            for char in s:
                freq[ord(char)-ord('a')] += 1
            
            map[tuple(freq)].append(s)
        
        return [val for val in map.values()]

        
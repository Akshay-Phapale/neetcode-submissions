class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket count
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            freq[value].append(key)
        
        res = []

        for item in range(len(freq)-1, 0, -1):
            for num in freq[item]:
                res.append(num)
                if (len(res) == k):
                    return res
        
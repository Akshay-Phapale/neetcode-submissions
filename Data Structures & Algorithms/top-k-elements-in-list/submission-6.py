class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap

        # count = {}

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # heap = []

        # for key, value in count.items():
        #     heapq.heappush(heap, (value, key))
        #     if (len(heap) > k):
        #         heapq.heappop(heap)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res
        
        # bucket 

        bucket = [[] for i in range(len(nums) + 1)]

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for key, val in count.items():
            bucket[val].append(key)

        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
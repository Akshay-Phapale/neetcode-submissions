class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            required = target - n
            if required in map:
                return [map[required], i]
            else: 
                map[n] = i
        
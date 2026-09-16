class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = max(piles)

        while left <= right:
            mid = (left + right) // 2

            timeNeeded = 0

            for pile in piles:
                timeNeeded += math.ceil(float(pile)/mid)
            
            if timeNeeded > h:
                left = mid + 1
            else:
                right = mid - 1
                res = min(res, mid)
            

        return res
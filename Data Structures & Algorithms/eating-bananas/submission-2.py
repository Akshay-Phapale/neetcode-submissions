class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        left, right = 1, max(piles)

        while left <= right:

            mid = (left + right) // 2

            time = 0

            for pile in piles:
                time =  time + math.ceil(float(pile)/mid)
            
            if time > h:
                left = mid + 1
            else:
                right = mid - 1
                res = min(res, mid)

        return res
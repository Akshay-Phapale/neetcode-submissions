class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = max(piles)

        while l<=r:
            mid = (l+r)//2
            timeNeeded = 0
            for pile in piles:
                timeNeeded += math.ceil(float(pile) / mid)

            if timeNeeded > h:
                l = mid + 1
            else:
                r = mid - 1
                res = min(res, mid)

        return res
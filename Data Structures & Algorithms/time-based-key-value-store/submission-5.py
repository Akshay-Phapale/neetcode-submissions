class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        timeToValue = self.map.get(key, [])
        l, r = 0, len(timeToValue)-1
    
        while l<=r:
            mid = (l+r) // 2
            time, value = timeToValue[mid]

            if time > timestamp:
                r = mid - 1
            else:
                res = value
                l = mid + 1


        return res
class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        timeToValue = self.map.get(key, [])
        timeToValue.append((timestamp, value))
        self.map[key] = timeToValue

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        timeToValue = self.map.get(key)
        l, r = 0, len(timeToValue)-1
        res = ""
        delta = float("inf")
        while l<=r:
            mid = (l+r) // 2
            time, value = timeToValue[mid]

            if time > timestamp:
                r = mid - 1
            else:
                if delta > timestamp - time:
                    delta = timestamp - time
                    res = value
                l = mid + 1


        return res
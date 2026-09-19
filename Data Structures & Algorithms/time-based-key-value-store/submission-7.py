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
        left, right = 0, len(timeToValue) - 1

        while left<= right:

            mid = (left + right) // 2
            time, value = timeToValue[mid]
            if time > timestamp:
                right = mid - 1
            else:
                left = mid + 1
                res = value

        return res
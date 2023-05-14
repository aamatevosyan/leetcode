from bisect import bisect_right

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
            self.store[key] = []
        
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store or self.store[key][0][0] > timestamp:
            return ""
        
        ind = bisect_right(self.store[key], timestamp, key=lambda x: x[0])
        
        return self.store[key][ind - 1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
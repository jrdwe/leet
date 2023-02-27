class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: 
            return ""
            
        entries, out = self.store[key], ""
        
        low, high = 0, len(entries) - 1
        while low <= high:
            mid  = low + (high - low) // 2
            v, t = self.store[key][mid]
            
            if timestamp >= t:
                out  = v
                low  = mid + 1
            else:
                high = mid - 1
        
        return out



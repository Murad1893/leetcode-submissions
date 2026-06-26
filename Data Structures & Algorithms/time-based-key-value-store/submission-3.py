class TimeMap:

    def __init__(self):
        self.datamap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.datamap[key].append([timestamp, value])
        print(self.datamap)

    def get(self, key: str, timestamp: int) -> str:
      
        if key not in self.datamap:
            return ""
        
        arr = self.datamap[key]
        
        # apply binary search on the value
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = l + (r-l) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        return arr[r][1] if r >= 0 else "" # similar to bisect_right check

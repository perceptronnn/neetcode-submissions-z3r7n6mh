class TimeMap:

    def __init__(self):
        self.kTs = {}
        self.kTsVs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kTs:
            self.kTs[key] = []
            self.kTsVs[key] = {}
        self.kTs[key].append(timestamp)
        self.kTsVs[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kTs:
            return ""
        ts = self.search(self.kTs[key], timestamp)
        if ts == "":
            return ""
        return self.kTsVs[key][ts]
        
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return target
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return nums[r] if r != -1 else ""
        

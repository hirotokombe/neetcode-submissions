class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        result = ""

        lst = self.map[key]

        l, r = 0, len(lst) - 1

        while l <= r:
            m = (l + r) // 2
            
            if lst[m][1] <= timestamp:
                result = lst[m][0]
                l = m + 1
            else: 
                r = m - 1

        return result
        



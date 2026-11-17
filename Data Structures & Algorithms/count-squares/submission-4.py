class CountSquares:

    def __init__(self):
        self.pointCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        px, py = point
        for x, y in self.points:
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            
            count += self.pointCount.get((px, y), 0) * self.pointCount.get((x, py), 0)
        return count

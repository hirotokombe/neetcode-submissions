class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        numFleets = 1
        currentCar = None
        trueHoursToFinish = float('-inf')

        positionSpeed = list(zip(position, speed))
        positionSpeed.sort(key=lambda x : x[0])

        while len(positionSpeed) > 1:
            currentCar = positionSpeed.pop()
            trailingCar = positionSpeed[-1]

            hoursToFinish1 = (target - currentCar[0]) / currentCar[1]
            hoursToFinish2 = (target - trailingCar[0]) / trailingCar[1]

            trueHoursToFinish = max(trueHoursToFinish, hoursToFinish1)

            if hoursToFinish2 > trueHoursToFinish:
                numFleets += 1

        return numFleets
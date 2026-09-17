class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carInfo = [(position[i], speed[i]) for i in range(len(position))]
        carInfo.sort(reverse=True, key=lambda x : x[0])
        stack = []

        for pos, speed in carInfo:
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) > 1 and time <= stack[-2]:
                stack.pop()
                
        return len(stack)
            


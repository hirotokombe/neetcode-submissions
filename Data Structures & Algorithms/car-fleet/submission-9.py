class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        stack = []

        for position, speed in cars:
            time = (target - position) / speed
            if not stack or not stack[-1] >= time:
                stack.append(time)
        
        return len(stack)
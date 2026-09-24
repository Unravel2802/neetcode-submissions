class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = list(zip(position, speed))
        car.sort(key=lambda x: x[0], reverse=True)
        stack = []

        for pos, speed in car:
            time = (target - pos) / speed

            if not stack or stack[-1] < time:
                stack.append(time)
            
        return len(stack)
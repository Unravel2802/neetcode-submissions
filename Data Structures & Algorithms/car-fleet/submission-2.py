class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort()
        stack = []

        # monotonic stack of time reach to target: from high to low. 
        # need to sort to make the higher time to the front
        for position, speed in reversed(cars):
            time = (target - position) / speed
            
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)

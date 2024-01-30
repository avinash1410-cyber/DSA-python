class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        
        # Create pairs of position and speed for each car
        for x in range(len(speed)):
            pairs.append([position[x], speed[x]])
        
        # Sort the pairs based on position in descending order
        pairs = sorted(pairs)[::-1]
        
        # Iterate through the sorted pairs
        for p, s in pairs:
            # Calculate time to reach the target for the current car
            time = (target - p) / s
            
            # Add the time to the stack
            stack.append(time)
            
            # Check if there are at least two cars in the stack and the current car
            # takes less or equal time than the previous car. If so, pop the previous car.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # The length of the stack represents the number of car fleets
        return len(stack)
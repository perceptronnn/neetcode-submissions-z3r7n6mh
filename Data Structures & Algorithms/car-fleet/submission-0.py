class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        positionTime = []
        for idx in range(len(position)):
            positionTime.append((position[idx], (target - position[idx])/speed[idx]))
        
        positionTime.sort()
        print(positionTime)
        fleetCount = 0
        fleetStack = []
        for item in reversed(positionTime):
            if len(fleetStack) == 0:
                fleetStack.append(item[1])
                continue
            if item[1] > fleetStack[-1]:
                fleetStack.append(item[1])
        return len(fleetStack)

        
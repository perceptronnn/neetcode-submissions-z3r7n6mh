class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []

        warmer = [0] * len(temperatures)
        yetToBeFound = [0]
        for idx in range(1, len(temperatures)):
            print(warmer)
            print(yetToBeFound)
            while len(yetToBeFound) > 0 and temperatures[idx] > temperatures[yetToBeFound[-1]]:
                i = yetToBeFound.pop()
                warmer[i] = idx - i
            yetToBeFound.append(idx)
        return warmer

        
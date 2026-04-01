class MinStack:

    def __init__(self):
        self.stack = [float('inf')]
        self.mins = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins.append(self.mins[-1] if self.mins[-1] < val else val)
        return None

    def pop(self) -> None:
        if len(self.stack) > 1:
            del self.stack[-1]
            del self.mins[-1]
        return None

    def top(self) -> int:
        if len(self.stack) > 1:
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        if len(self.mins) > 1:
            return self.mins[-1]
        return None
        

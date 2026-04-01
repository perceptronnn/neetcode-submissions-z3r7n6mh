class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        mainStack = []
        auxilaryStack = []
        for token in reversed(tokens):
            mainStack.append(token)
        
        while len(mainStack) > 1 and mainStack[0] in operators:
            print(mainStack, auxilaryStack)
            while mainStack[-1] not in operators:
                auxilaryStack.append(int(mainStack.pop()))
            
            op = mainStack.pop()
            rhs = auxilaryStack.pop()
            lhs = auxilaryStack.pop()
            print(lhs, rhs, op)
            if op == '+':
                mainStack.append(lhs + rhs)
            elif op == '-':
                mainStack.append(lhs - rhs)
            elif op == '*':
                mainStack.append(lhs * rhs)
            else:
                mainStack.append(int(lhs / rhs))
        return int(mainStack[0])

        
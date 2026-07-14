class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            print(stack)
            if op == 'C':
                if not stack:
                    return None
                stack.pop()
            elif op == '+':
                if len(stack) < 2:
                    return None
                newScore = stack[-1] + stack[-2]
                stack.append(newScore)
            elif op == 'D':
                if not stack:
                    return None
                newScore = stack[-1] * 2
                stack.append(newScore)
            else:
                stack.append(int(op))
        total = 0
        for score in stack:
            total += score
        return total
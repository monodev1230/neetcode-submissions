class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in '{([':
                stack.append(p)
            else:
                if not stack:
                    return False

                if p == '}' and stack[-1] != '{':
                    return False
                elif p == ')' and stack[-1] != '(':
                    return False
                elif p == ']' and stack[-1] != '[':
                    return False
                stack.pop()

        return len(stack) == 0
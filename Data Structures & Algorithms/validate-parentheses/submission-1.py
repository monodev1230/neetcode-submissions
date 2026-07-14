class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == '{' or p == '[' or p =='(':
                stack.append(p)
            else:
                if not stack:
                    return False

                if p == '}':
                    if stack[-1] != '{':
                        return False
                elif p == ')':
                    if stack[-1] != '(':
                        return False
                else:
                    if stack[-1] != '[':
                        return False
                stack.pop()

        return len(stack) == 0
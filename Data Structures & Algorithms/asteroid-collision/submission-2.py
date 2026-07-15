class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0 
        while i < len(asteroids):
            if stack and stack[-1] > 0 and asteroids[i] < 0:
                collision = stack[-1] + asteroids[i]
                if collision < 0:
                    stack.pop()
                    continue
                elif collision == 0:
                    stack.pop()
            else:
                stack.append(asteroids[i])
            i += 1
        return stack

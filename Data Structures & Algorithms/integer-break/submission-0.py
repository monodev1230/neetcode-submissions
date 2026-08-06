class Solution:
    def integerBreak(self, n: int) -> int:
        # 2 -> 2
        # 3 -> 2 1 -> 2
        # 4 -> 2 2 -> 4
        # 5 -> 2 3 -> 6
        # 6 -> 3 3 -> 9
        # 7 -> 2 3 2 -> 12
        # 8 -> 2 2 2 2 -> 16, 3 3 2 -> 18
        # 9 -> 3 3 3 -> 27, 2 2 2 3 
        # 10 -> 2 2 3 3 -> 36
        # 14 -> 3 3 3 3 2 -> 162, 3 3 2 2 2 2
        if n > 3: 
            if n % 3 == 0:
                return 3 ** (n//3)
            elif n % 3 == 1:
                return 3 ** (n//3 - 1) * 4
            else:
                return 3 ** (n//3) * 2
        elif n == 3:
            return 2
        elif n ==2 :
            return 1
        
        
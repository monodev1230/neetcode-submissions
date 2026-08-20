class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        countFive = 0
        countTen = 0

        for bill in bills:
            if bill == 5:
                countFive += 1
            elif bill == 10:
                if countFive < 1:
                    return False
                countFive -= 1
                countTen += 1
            else:
                if (countTen >= 1 and countFive >= 1) or countFive >= 3:
                    if countTen > 0:
                        countTen -= 1
                        countFive -= 1
                    else:
                        countFive -= 3
                else:
                    return False
        return True
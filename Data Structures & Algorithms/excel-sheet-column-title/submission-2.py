class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ''
        res = []
        n = columnNumber
        while n:
            n -= 1
            res.append(chr(n%26 + ord('A')))
            n = n // 26
        return ''.join(res[::-1])


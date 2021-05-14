class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        ALF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        while columnNumber > 26:
            cel = columnNumber // 26
            ost = columnNumber % 26
            if ost == 0:
                ost = 26
                cel -= 1
            columnNumber = cel
            result += ALF[ost-1]

        if columnNumber > 0:
            result += ALF[columnNumber-1]
        return result[::-1]

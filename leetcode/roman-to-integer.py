class Solution:
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s: str) -> int:
        total = 0

        i = 0
        while i < len(s):
            curr = s[i:]

            sym = self.getSymbol(curr)
            total += self.values[sym]

            i += len(sym)

        return total


    def getSymbol(self, s: str) -> str:
        if s[0] == 'I':
            if len(s) > 1:
                d = s[1]
                if d == 'V':
                    return 'IV'
                if d == 'X':
                    return 'IX'
            return 'I'

        if s[0] == 'X':
            if len(s) > 1:
                d = s[1]
                if d == 'L':
                    return 'XL'
                if d == 'C':
                    return 'XC'
            return 'X'

        if s[0] == 'C':
            if len(s) > 1:
                d = s[1]
                if d == 'D':
                    return 'CD'
                if d == 'M':
                    return 'CM'
            return 'C'

        return s[0]

s= Solution()
x = s.romanToInt('III')
print(x)
class Solution:
    def myAtoi(self, s: str) -> int:
        # Read in and ignore any leading whitespace.
        s = s.lstrip()

        # Check if the next character (if not already at the end
        # of the string) is '-' or '+'.
        if s == "":
            return 0
        
        isNegative = False
        if s[0] == "-":
            isNegative = True

        if s[0] == "-" or s[0] == "+":
            s = s[1:]
        
        # Read in next the characters until the next non-digit
        # character or the end of the input is reached. The rest
        # of the string is ignored.
        atoi = 0
        while s != "":
            c = s[0]
            
            if not self.isDigit(c):
                break
            
            atoi *= 10
            atoi += int(c)

            s = s[1:]

        # If the integer is out of the 32-bit signed integer range
        # [-231, 231 - 1], then clamp the integer so that it
        # remains in the range. Specifically, integers less than
        # -231 should be clamped to -231, and integers greater than
        # 231 - 1 should be clamped to 231 - 1.
        if isNegative:
            atoi *= -1

            if atoi < -2 ** 31:
                return -2 ** 31
        
        if atoi > 2 ** 31 - 1:
            return 2 ** 31 - 1

        # Return the integer as the final result.
        return atoi

    def isDigit(self, c: str):
        return ord(c) > 47 and ord(c) < 58

print(Solution().myAtoi("   -42"))
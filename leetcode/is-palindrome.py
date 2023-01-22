class Solution:
    def isPalindrome(self, x: int) -> bool:
        xString = str(x)
        xStringReversed = xString[::-1]

        for i in range(len(xString)):
            if xString[i] != xStringReversed[i]:
                return False
        
        return True
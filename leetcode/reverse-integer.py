class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        if isNegative:
            x *= -1

        answer = 0
        while x > 0:
            answer *= 10

            current = x % 10
            answer += current

            x -= current
            x //= 10

        if answer > 2**31:
            return 0
        
        if isNegative:
            return answer * -1
            
        return answer

print(Solution().reverse(123))
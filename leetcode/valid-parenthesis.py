class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return True
        if len(s) == 1: return False

        stack = Stack()

        left = ['[', '{', '(']
        right = [']', '}', ')']

        for c in s:
            if c in left:
                stack.push(c)
                continue

            if c in right:
                if stack.length() == 0:
                    return False

                curr = stack.pop()
                if curr not in left:
                    return False
                
                if (c == ']' and curr == '[') or (c == '}' and curr == '{') or (c == ')' and curr == '('):
                    continue

                return False
        
        if stack.length() != 0:
            return False
        
        return True


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack += value

    def pop(self):
        value = self.stack[-1]
        self.stack = self.stack[:-1]
        return value
    
    def length(self):
        return len(self.stack)

    
s = '()'
sol = Solution()
print(sol.isValid(s))
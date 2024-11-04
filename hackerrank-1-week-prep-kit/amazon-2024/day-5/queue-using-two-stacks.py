# Enter your code here. Read input from STDIN. Print output to STDOUT
class Stack:   
    def __init__(self):
        self.data = []
        
    def push(self, val):
        self.data.append(val)
        
    def pop(self):
        if len(self.data) == 0:
            return None
            
        val = self.data[-1]
        self.data = self.data[:-1]
        return val
        
    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]
        
class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def enqueue(self, val):
        self.stack1.push(val)
        
    def dequeue(self):
        self.shift_stacks()
        return self.stack2.pop()
        
    def peek(self):
        self.shift_stacks()
        return self.stack2.peek()
        
    def shift_stacks(self):
        if len(self.stack2.data) > 0:
            return
            
        while True:
            x = self.stack1.pop()
            if x is None:
                break
            self.stack2.push(x)
        
        
if __name__ == '__main__':
    q = Queue()
    
    tests = int(input())
    
    for _ in range(tests):
        test = input()
        if test[0] == '1':
            testArr = test.split(' ')
            q.enqueue(testArr[1])
        elif test == '2':
            q.dequeue()
        elif test == '3':
            print(q.peek())
        

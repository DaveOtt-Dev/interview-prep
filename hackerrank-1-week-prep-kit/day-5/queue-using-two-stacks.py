# Enter your code here. Read input from STDIN. Print output to STDOUT
enqueue = 1
dequeue = 2
printFront = 3


class Stack:
    def __init__(self):
        self.__stack = []
        
    def push(self, value):
        self.__stack.append(value)
        
    def pop(self):
        return self.__stack.pop()
        
    def get(self, index):
        return self.__stack[index]
        
    def length(self):
        return len(self.__stack)
        
    def print(self):
        print(self.__stack)


class Queue:
    def __init__(self):
        self.__masterStack = Stack()
        
    def print(self):
        self.__masterStack.print()
        
    def enqueue(self, value):
        self.__masterStack.push(value)

    def dequeue(self):
        storageStack = Stack()
        
        while self.__masterStack.length() > 0:
            storageStack.push(self.__masterStack.pop())
            
        returnVal = storageStack.pop()
        
        while storageStack.length() > 0:
            self.__masterStack.push(storageStack.pop())
            
        return returnVal
        
    def printFront(self):
        storageStack = Stack()
        
        while self.__masterStack.length() > 0:
            storageStack.push(self.__masterStack.pop())
            
        printVal = storageStack.pop()
        self.__masterStack.push(printVal)
        
        while storageStack.length() > 0:
            self.__masterStack.push(storageStack.pop())
            
        print(printVal)

    
if __name__ == "__main__":
    q = int(input())
    
    queue = Queue()
    
    for _ in range(q):
        stdin = input().strip().split(" ")
        
        query = int(stdin[0])   
        
        if query == dequeue:
            queue.dequeue()
        elif query == printFront:
            queue.printFront()
        else:
            value = stdin[1]
            queue.enqueue(value)
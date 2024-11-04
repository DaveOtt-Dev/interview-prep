# Enter your code here. Read input from STDIN. Print output to STDOUT

class Editor:
    
    def __init__(self):
        self.S = ''
        self.history = []
        
    def append(self, W):
        self.history.append(self.S[::])
        self.S += W
        
    def delete(self, k):
        self.history.append(self.S[::])
        self.S = self.S[:-k]
        
    def print(self, k):
        print(self.S[k-1])
        
    def undo(self):
        self.S = self.history.pop()

e = Editor()

Q = int(input())
for _ in range(Q):
    test = input()
    if test[0] == '1':
        e.append(test.split(' ')[1])
    elif test[0] == '2':
        e.delete(int(test.split(' ')[1]))
    elif test[0] == '3':
        e.print(int(test.split(' ')[1]))
    elif test[0] == '4':
        e.undo()
    # print(e.S, e.history)
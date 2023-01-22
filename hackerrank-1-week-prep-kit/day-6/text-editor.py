class Command:
    def __init__(self, op, impactedText=None):
        self.op = op
        self.impactedText = impactedText
        
    def getOppositeOperation(self):
        if self.op == 1:
            return f"2 {len(self.impactedText)}"
        if self.op == 2:
            return f"1 {self.impactedText}"

class TextEditor:
    def __init__(self):
        self.s = ""
        self.__opHist = []
        
    def execCommand(self, command, isUndo=False):
        splitCommand = command.split(" ")
        op = int(splitCommand[0])
        
        if op == 4:
            return self.__undo()
        
        val = splitCommand[1]
        myCommand = Command(op)
        if op == 1:
            if not isUndo:
                myCommand.impactedText = val
                self.__opHist.append(myCommand)
            
            self.__append(val)
        elif op == 2:
            k = int(val)
            if not isUndo:
                myCommand.impactedText = self.s[-k:]
                self.__opHist.append(myCommand)
            
            self.__delete(k)
        elif op == 3:
            self.__print(int(val))
        
    def __append(self, w):
        self.s += w
        
    def __delete(self, k):
        self.s = self.s[0:-k]
        
    def __print(self, k):
        print(self.s[k-1])
        
    def __undo(self):
        oppositeOperation = self.__opHist.pop().getOppositeOperation()
        self.execCommand(oppositeOperation, isUndo=True)


if __name__ == "__main__":
    q = 8
    
    textEditor = TextEditor()
    commands = [
        "1 abc", 
        "3 3", 
        "2 3", 
        "1 xy",
        "3 2",
        "4",
        "4",
        "3 1"
    ]
    for command in commands:
        textEditor.execCommand(command)
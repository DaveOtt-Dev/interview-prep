class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def append(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            curr = self.root
            while curr.next != None:
                curr = curr.next

            curr.next = Node(val)

    def reverse(self):
        curr = self.root
        prev = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        self.root = prev

    def print(self):
        outputStr = '['

        curr = self.root
        while curr != None:
            outputStr += str(curr.value) + ','
            curr = curr.next
        
        outputStr = outputStr[:-1] + ']'
        print(outputStr)


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)

l.print()
l.reverse()
l.print()
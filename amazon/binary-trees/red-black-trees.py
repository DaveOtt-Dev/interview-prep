class Node:
    def __init__(self, data=None):
        self.data = data
        self.color = None
        self.parent = None
        self.left = None
        self.right = None
    
    def grandparent(self):
        return self.parent.parent
    
    def uncle(self):
        try:
            if self.parent.parent.left != self.parent:
                return self.parent.parent.left
            else:
                return self.parent.parent.right
        except:
            return None

class RedBlackTree:
    def __init__(self, root: Node):
        self.root = root

    def insert(self, value):
        node = Node(value)
        node.color = 'black'

        if self.root is None:
            self.root = node
            return True

        while True:
            curr = queue[0]
            queue = queue[1:]

            if node.data <= curr.data:
                if curr.left is None:
                    curr.left = node
                    node.parent = curr.left
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                    node.parent = curr.right
                    break
                curr = curr.right

        # uncle is grandparents other child
        if node.parent.color == 'red':
            



    def search(self):
        pass

    def delete(self):
        pass

    def rotate(self):
        pass
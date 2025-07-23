class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, num):
        node = Node(num)

        if self.root is None:
            self.root = node
            return
        
        queue = [self.root]
        while len(queue) > 0:
            curr = queue[0]
            queue = queue[1:]

            if curr.left is None:
                curr.left = node
                return
            if curr.right is None:
                curr.right = node
                return
            
            queue.append(curr.left)
            queue.append(curr.right)

    def depthFirstSearch(self, mode='inOrder'):
        if mode == 'inOrder':
            return self.__inOrderTraversal(self.root)
        if mode == 'preOrder':
            return self.__preOrderTraversal(self.root)
        if mode == 'postOrder':
            return self.__postOrderTraversal(self.root)

    def __inOrderTraversal(self, curr):
        if curr is None:
            return []
        return self.__inOrderTraversal(curr.left) + [curr.data] + self.__inOrderTraversal(curr.right)

    def __preOrderTraversal(self, curr):
        if curr is None:
            return []
        return [curr.data] + self.__preOrderTraversal(curr.left) + self.__preOrderTraversal(curr.right)

    def __postOrderTraversal(self, curr):
        if curr is None:
            return []
        return self.__preOrderTraversal(curr.left) + self.__preOrderTraversal(curr.right) + [curr.data]
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        node = Node(value)

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

    def __preOrderTraversal(self, curr):
        if curr is None:
            return []

        return [curr.data] + self.__preOrderTraversal(curr.left) + self.__preOrderTraversal(curr.right)

    def __inOrderTraversal(self, curr):
        if curr is None:
            return []

        return self.__inOrderTraversal(curr.left) + [curr.data] + self.__inOrderTraversal(curr.right)

    def __postOrderTraversal(self, curr):
        if curr is None:
            return []

        return self.__postOrderTraversal(curr.left) + self.__postOrderTraversal(curr.right) + [curr.data]

    def breadthFirstSearch(self):
        bfs = []
        queue = [self.root]

        while len(queue) > 0:
            curr = queue[0]
            queue = queue[1:]

            if curr is None:
                continue

            bfs.append(curr.data)
            queue.append(curr.left)
            queue.append(curr.right)

        return bfs

    def search(self, value):
        if self.root is None:
            return False

        if self.root.data is value:
            return True

        queue = [self.root]
        while len(queue) > 0:
            curr = queue[0]
            queue = queue[1:]

            if curr.left is None:
                continue
            if curr.left.data is value:
                return True

            if curr.right is None:
                continue
            if curr.right.data is value:
                return True
            
            queue.append(curr.left)
            queue.append(curr.right)

        return False

    def delete(self, value):
        if self.root is None:
            return False
        
        # 1. find the target node
        targetNode = None
        if self.root.data == value:
            targetNode = self.root

        queue = [self.root]
        while len(queue) > 0:
            curr = queue[0]
            queue = queue[1:]

            if curr.left is None:
                continue
            if curr.left.data == value:
                targetNode = curr.left
                break

            if curr.right is None:
                continue
            if curr.right.data == value:
                targetNode = curr.right
                break
            
            queue.append(curr.left)
            queue.append(curr.right)

        # 2. find the last parent node in the tree, bookmark it, and remove its rightmost child
        lastParent = None
        queue = [self.root]
        while len(queue) > 0:
            curr = queue[0]
            queue = queue[1:]

            if curr.left is not None or curr.right is not None:
                lastParent = curr
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

        # 3. replace the target node with the last node
        if lastParent is None:
            return False
        if lastParent.right is not None:
            targetNode.data = lastParent.right.data
            lastParent.right = None
            return True
        if lastParent.left is not None:
            targetNode.data = lastParent.left.data
            lastParent.left = None
            return True

        
        return False   

# # Initialize and allocate memory for tree nodes
# firstNode = Node(2)
# secondNode = Node(3)
# thirdNode = Node(4)
# fourthNode = Node(5)

# # Connect binary tree nodes
# firstNode.left = secondNode
# firstNode.right = thirdNode
# secondNode.left = fourthNode

# tree = BinaryTree(firstNode)

# # Depth-first searches:
# print(f'Pre-order DFS: {tree.depthFirstSearch('preOrder')}')
# print(f'In-order DFS: {tree.depthFirstSearch('inOrder')}')
# print(f'Post-order DFS: {tree.depthFirstSearch('postOrder')}')

# # Breadth-first search:
# print(f'Level order: {tree.breadthFirstSearch()}')

# Insertion:
tree = BinaryTree()
for i in range(10):
    tree.insert(i)

print(f'Level order: {tree.breadthFirstSearch()}')

print(f'Search 5: {tree.search(5)}')
print(f'Search 101: {tree.search(101)}')

print(f'Delete 3: {tree.delete(3)}')
print(f'Level order: {tree.breadthFirstSearch()}')
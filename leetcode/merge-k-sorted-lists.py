# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        curr = self.root
        while(True):
            if val < curr.val:
                if curr.left is None:
                    curr.left = Node(val)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(val)
                    break
                curr = curr.right

    def inOrder(self):
        return self.inOrderHelper(self.root)

    def inOrderHelper(self, curr):
        if curr is None:
            return []

        return self.inOrderHelper(curr.left) + [curr.val] + self.inOrderHelper(curr.right)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        tree = BST()

        for ln in lists:
            temp = ln
            while temp is not None:
                tree.insert(temp.val)
                temp = temp.next 
        
        asList = tree.inOrder()
        if len(asList) == 0:
            return None

        returnNode = ListNode(asList[0])
        asList = asList[1:]

        temp = returnNode
        for num in asList:
            temp.next = ListNode(num)
            temp = temp.next

        return returnNode
        
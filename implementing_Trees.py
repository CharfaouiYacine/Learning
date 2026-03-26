class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
            return
        else:
            current = self.root
            new_node = Node(value)
            while True:
                if value <= current.value :
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
    def search(self,value):
        if self.root is None:
            return "Tree is empty"
        else:
            current = self.root
            while current is not None:
                if current.value == value:
                    return current
                elif value < current.value:
                    current = current.left
                else:
                    current = current.right
            return None

    # ----------------------------------------------------#
    # This functions are for traversal (inorder,preorder,postorder)
    """inorder traversal uses the following rule: visit node.left --> visit node --> visit node.right
     this function uses  recursion with the base case set as : if node is none return nothing"""

    def inorder_traversal(self,node):
        if node is None:
            return
        else:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)

    """preorder traversal uses the following rule: visit node --> visit node.left --> visit node.right
         this function uses  recursion with the base case set as : if node is none return nothing"""
    def preorder_traversal(self,node):
        if node is None:
            return
        else:
            print(node.value)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    """postorder traversal uses the following rule: visit node.left --> visit node.right --> visit node
         this function uses  recursion with the base case set as : if node is none return nothing"""
    def postorder_traversal(self,node):
        if node is None:
            return
        else:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value)

    # ----------------------------------------------------#
    # This functions are used in the delete function (to be more clean)
    def search_node_and_parent(self,value):
        if self.root is None:
            return "Tree is empty"
        else: # find the node to delete and it's parent
            current = self.root
            parent = None
            while current is not None:
                if current.value == value:
                    return current,parent
                elif value < current.value:
                    parent = current
                    current = current.left
                else:
                    parent = current
                    current = current.right
            return None,None

    def find_successor(self,node):
        # we didn't check for empty case because if it reaches this  level it has to have two children
        """ this method uses the right subtree of the node that we want to delete  so it fetches us the
        lowest value in the right subtree  with its parent so we can  delete this node after taking its value"""
        successor = node.right
        s_parent = None
        while successor.left is not None:
            s_parent = successor
            successor = successor.left
        return successor, s_parent

    # ----------------------------------------------------#
    def delete_node(self,value):
        current,parent = self.search_node_and_parent(value)
        if current is None: # when node doesn't exist
            print("Node does not exist")
        # ----------------------------------------------------#
        elif current.left is None and current.right is None: # first case : no children
            if parent is None: # means the node is a root
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
        # ----------------------------------------------------#
        elif current.left is not None and current.right is None:# Second case: one child (left)
            if parent is None:
                self.root = current.left
            else:
                if parent.left == current:
                    parent.left = current.left
                else:
                    parent.right = current.left

        elif current.right is not None and current.left is None:# Second case: one child (right)
            if parent is None:
                self.root = current.right
            else:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
        # ----------------------------------------------------#
        else: # third case : two children
            # we used the method of successor ( lowest value in the right SubTree)
            successor,s_parent = self.find_successor(current)
            if current.right == successor:  # here we didn't use the s_parent because it is the same as current ( both are parents to successor)
                if successor.right is None:
                    current.value = successor.value
                    current.right = None
                else:
                    current.value = successor.value
                    current.right = successor.right
            else: # successor is somewhere in the right subtree
                if successor.right is not None: # successor have a right child
                    current.value = successor.value
                    s_parent.left = successor.right
                else: # means that successor doesn't have any children
                    current.value = successor.value
                    s_parent.left = None

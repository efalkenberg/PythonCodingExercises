import random as r


class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return self._formatted(0)
    
    def _formatted(self, level):
        fmt = "\t"*level + str(self.data) + "\n"

        if self.left is None:
            fmt += "\t"*(level+1) + "[END]\n"
        else:
            fmt += self.left._formatted(level+1)

        if self.right is None:
            fmt += "\t"*(level+1) + "[END]\n"
        else:
            fmt += self.right._formatted(level+1)
        
        return fmt

class BinarySearchTree(Node):
    def append(self, value):
        if value < self.data:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.append(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:   
                self.right.append(value)


class NodeUtil(object):

    @staticmethod
    def create_full_balanced_tree(max_depth=3):
        if max_depth == 0:
            return None

        node = Node(int(r.random()*100)) 
        node.left = NodeUtil.create_full_balanced_tree(max_depth-1)
        node.right = NodeUtil.create_full_balanced_tree(max_depth-1)
        return node

    @staticmethod
    def create_bst(nodes_count=30):
        root = BinarySearchTree(42)
        for i in range(1, nodes_count):
            root.append((int(r.random()*100)))
        return root

    @staticmethod 
    def depth(node):
        node_left_depth = 0
        node_right_depth = 0
        if node.left is not None:
            node_left_depth = NodeUtil.depth(node.left) 
        if node.right is not None:
            node_right_depth = NodeUtil.depth(node.right)
        max_depth = max(node_left_depth, node_right_depth)

        return max_depth + 1

    @staticmethod
    def depth_first_search(node, value, verbose=False):
        found = False
        if node.left is not None:
            found = NodeUtil.depth_first_search(node.left, value)
            if found:
                return True
        if node.data == value:
            return True
        if node.right is not None:
            found = NodeUtil.depth_first_search(node.right, value)
            if found:
                return True
        return False

    @staticmethod
    def bst_to_linked_list(node, linked_list=None):
        # left child
        if node.left is not None:
            linked_list = NodeUtil.bst_to_linked_list(node.left, linked_list)
        
        # self
        linked_list.append_end(node.data)

        # right child
        if node.right is not None:
            linked_list = NodeUtil.bst_to_linked_list(node.right, linked_list)

        return linked_list

        




        



    




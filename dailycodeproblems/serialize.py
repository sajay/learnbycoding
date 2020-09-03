#This problem was asked by Google.
#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.
#For example, given the following Node class
#class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#       self.right = right
#The following test should pass:
#node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

# Serialization is to store tree in a file so that it can be later restored. 
# The structure of tree must be maintained. 
# Deserialization is reading tree back from file.

#Depth First Traversals:
#(a) Inorder (Left, Root, Right) : 4 2 5 1 3
#(b) Preorder (Root, Left, Right) : 1 2 4 5 3
#(c) Postorder (Left, Right, Root) : 4 5 2 3 1
#Breadth First or Level Order Traversal : 1 2 3 4 5

# function serialize which stores the tree into an array A[ ] and 
# deSerialize which deserializes the array to tree and returns it.
# Note: The structure of tree must be maintained.

# Algorithm Inorder(tree)
#   1. Traverse the left subtree, i.e., call Inorder(left-subtree)
#   2. Visit the root.
#   3. Traverse the right subtree, i.e., call Inorder(right-subtree)
# Uses of Inorder
# In case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. 
# To get nodes of BST in non-increasing order, a variation of Inorder traversal 
# where Inorder traversal s reversed can be used.

#Algorithm Preorder(tree)
#   1. Visit the root.
#   2. Traverse the left subtree, i.e., call Preorder(left-subtree)
#   3. Traverse the right subtree, i.e., call Preorder(right-subtree) 
#Uses of Preorder
#Preorder traversal is used to create a copy of the tree. 
# Preorder traversal is also used to get prefix expression on of an expression tree. 
#Please see http://en.wikipedia.org/wiki/Polish_notation to know why prefix expressions are useful.

# Algorithm Postorder(tree)
#   1. Traverse the left subtree, i.e., call Postorder(left-subtree)
#   2. Traverse the right subtree, i.e., call Postorder(right-subtree)
#   3. Visit the root.
#Uses of Postorder
#Postorder traversal is used to delete the tree. 
#Postorder traversal is also useful to get the postfix expression of an expression tree. 
#Please see http://en.wikipedia.org/wiki/Reverse_Polish_notation to for the usage of postfix expression.

#1, 2, 3, 4, 5, #, #, 6
#As you can see, we have two ‘#’ characters, which are showing null node children ( left and right ) 
# for Node 3. It is done to save structure of the binary tree. 
# We basically saving our nodes in level format. 
# Something, which you are doing during BFS tree traversal.
# In our serialize function we are creating embedded encode function, which in case of node adds it to array of strings, 
# and in case not — adds # symbol.
# Deserilization function will look same, however will just read characters from array, and create 
# required nodes.

def serialize(self, root):
        self.vals = []
        def encode(node):
            if node:
                self.vals.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                self.vals.append('#')
        
        encode(root)
        
        return ' '.join(self.vals)

def deserialize(self, data):
        
        def decode(vals):
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = decode(vals)
            node.right = decode(vals)
            return node
        
        vals = iter(data.split())
        return decode(vals)

# Solution 2

class Node:

    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


# This method serializes the tree into a string

def serialize(root):

    vals = []

    def encode(node):

        vals.append(str(node.val))

        if node.left is not None:

            encode(node.left)
        else:
            vals.append("L")

        if node.right is not None:

            encode(node.right)
        else:
            vals.append("R")

    encode(root)

    print(vals)
    return vals

# This method deserializes the string back into the tree

def deserialize(string_list):

    def create_a_tree(sub_list):

        if sub_list[0] == 'L' or sub_list[0] == 'R':
            del sub_list[0]
            return

        parent = Node(sub_list[0])
        del sub_list[0]

        parent.left = create_a_tree(sub_list)

        parent.right = create_a_tree(sub_list)

# To test
tree1 = Node('root', Node('left'), Node('right'))
t = deserialize(serialize(tree1))
print(str(t.right.val))
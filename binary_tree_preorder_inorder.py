"""
    Construct a binary tree given the preorder and inorder order of
        the tree as well as decode an encoded sequence.
"""

class BinaryTree():
    def __init__(self, value):
        """Instanstiates a BinaryTree object with its value attribute set to
            value and its left and right attributes set to None.
            
            Parameters: value is a string that represents a number.
            
            Returns: None."""
        self._value = value
        self._left = None
        self._right = None
    
    def __str__(self):
        """Represents the attribute value of a BinaryTree node as a string.
        
            Parameters: None.
            
            Returns: None."""
        return self._value

def create_tree(preorder, inorder):
    """Takes two lists, which represent the preorder and inorder
        representation of a binary tree and recursively reconstructs the
        binary tree.
        
        Paramters: preorder is a list of the elements in the binary tree
            in preorder order.
            inorder is a list of the elements in the binary tree in inorder
            order.
            
        Returns: The binary tree that is represented by its preorder and
            inorder."""
    if preorder == [] or inorder == []:
        return None
    else:
        x = BinaryTree(str(preorder[0]))
        index = inorder.index(preorder[0])
        x._left = create_tree(preorder[1 : index + 1], inorder[0 : index])
        x._right = create_tree(preorder[index + 1 : ] , inorder[index + 1 : ])
    return x

def decode_tree(tree, encoded):
    """Takes the encoded message and decodes it by getting the values
        that are represented.
        
        Paramters: tree is a Binary Tree object.
            encoded is a string of the encoded message.
        
        Returns: A string that is supposed to be the encoded message."""
    astring = ""
    x = tree
    while encoded != "":
        if encoded[0] == "0":
            if x._left != None:
                x = x._left
            else:
                x = tree
        elif encoded[0] == "1":
            if x._right != None:
                x = x._right
            else:
                x = tree
        if x._left == None and x._right == None:
            astring += x._value
            x = tree
        encoded = encoded[1:]
    return astring

def postorder_traversal(tree):
    """Takes a Binary Tree and prints out the traversal of the tree in
        postorder.
        
    Parameters: tree is a Binary Tree object.
    
    Returns: A string that represents the postorder traversal of the
        Binary Tree."""
    if tree._left == None and tree._right == None:
        return tree._value
    else:
        if tree._right == None:
            return postorder_traversal(tree._left) + " " + tree._value
        if tree._left == None:
            return postorder_traversal(tree._right) + " " + tree._value
        if tree._left != None and tree._right != None:
            return postorder_traversal(tree._left)+ " " + \
                postorder_traversal(tree._right) + " " + tree._value

def main():
    afile = open(input("Input file: "), "r")
    preorder = afile.readline().split()
    inorder = afile.readline().split()
    encoded = afile.readline()
    x = create_tree(preorder, inorder)
    print(postorder_traversal(x))
    print(decode_tree(x, encoded))

main()

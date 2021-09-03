from node import Node


##inverting the binary tree
def reverse (node):
    if node :
        node.left,node.right=node.right,node.left
        reverse (node.left)
        reverse (node.right)
        return node

## tree arithmetic
def tree_math(node1,node2,operation):
    if node1 and  node2 :
        if operation == '+':
            node2.data = node2.data + node1.data
            tree_math(node1.left, node2.left, operation)
            tree_math(node1.right, node2.right, operation)
        if operation == '-':
            node2.data = node2.data - node1.data
            tree_math(node1.left, node2.left, operation)
            tree_math(node1.right, node2.right, operation)
        if operation == '*':
            node2.data = node2.data * node1.data
            tree_math(node1.left, node2.left, operation)
            tree_math(node1.right, node2.right, operation)
        if operation == '/':
            node2.data = node2.data / node1.data
            tree_math(node1.left, node2.left, operation)
            tree_math(node1.right, node2.right, operation)
    



##test
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(400)
root.insert(31)
root.insert(42)
root.PrintTree()
root.find(400)
print(root.transverse(root))
roo = Node(27)
roo.insert(14)
roo.insert(35)
roo.insert(10)
roo.insert(400)
roo.insert(31)
roo.insert(42)
tree_math (root,roo,'+')
roo.PrintTree()
reverse(root)
print(root.transverse(root))







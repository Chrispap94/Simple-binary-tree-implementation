class Node:
    ## define tree node
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    ## insert into
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    ## find a value
    def find(self, value):
        c = "root"
        if self.data == value:
            print("match", c)
        if self.data < value:
            if self.right is None:
                print("no")
            else:
                c = c + ',right'
                self.right.find2(value,c)
        if self.data > value:
            if self.left is None:
                print("no")
            else:
                c = c + ',left'
                self.left.find2(value,c)
    ## +location
    def find2(self, value,c):

        if self.data == value:
            print("match", c)
        if self.data < value:
            if self.right is None:
                print("no")
            else:
                c = c + ',right'
                self.right.find2(value, c)
        if self.data > value:
            if self.left is None:
                print("no")
            else:
                c = c + ',left'
                self.left.find2(value, c)

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    ##In-order traversal
    def transverse (self,node):
        c=[]
        if node:
            c=c+self.transverse(node.left)
            c.append(node.data)
            c=c+self.transverse(node.right)
        return c


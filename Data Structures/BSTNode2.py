class Node:
    def __init__(self,data):
        self.left = self.right = None
        self.data = data

class BST:
    def __init__(self,data):
        self.head = Node(data) # set root

    def insert(self,data,curr=None):
        newNode = Node(data)
        if curr is None:
            curr = self.head
        if data < curr.data: # go left
            if curr.left is None: # empty space
                curr.left = newNode
            else:
                self.insert(data,curr.left)
        else:
            if curr.right is None:
                curr.right = newNode
            else:
                self.insert(data,curr.right)


    def search(self,target,curr): # recursive search
        if curr is None:
            return "Not found"
        
        elif data == curr.data:
            return "Found at {}".format(curr)
        elif data < curr.data:
            return self.search(data,curr.right)
        else:
            return self.search(data,curr.left)

    def lookup(self,target,curr="head",parent=None):
        if curr == "head":
            curr = self.head
        if curr is None:
            return None, None
        elif target == curr.data: # found
            return curr,parent
        elif target < curr.data:
            return self.lookup(target,curr.left,curr)
        else:
            return self.lookup(target,curr.right,curr)

    def delete(self,target):
        node, parent = self.lookup(target)
        if node:
            # 0 child
            if node.left == node.right == None:
                if parent.left is node: # check if node belongs to left or right of parent
                    parent.left = None
                else:
                    parent.right = None
                
            # 1 child
            elif (node.left is None) != (node.right is None):
                if node.left: # find left or right child of node
                    n = node.left
                else:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
            # 2 child
            # find smallest in right sub tree
            else:
                curr,succ = node,node.right
                while succ.left:
                    # terminates when succ is the smallest value (i.e. succ.left is None)
                    curr = succ
                    succ = succ.left
                node.data = succ.data # replace data but keep the links
                # adjust links
                if curr.left is succ:
                    curr.left = succ.right
                else:
                    curr.right = succ.left

                    
    def inorder(self,curr=None):
        if curr is None:
            curr = self.head # start from the head of BST
        if curr.left:
            self.inorder(curr.left)
        print(curr.data)
        if curr.right:
            self.inorder(curr.right)


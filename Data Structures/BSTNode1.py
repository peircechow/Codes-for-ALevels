class BST:
    def __init__(self,data):
        self.left = self.right = None
        self.data = data

    def insert(self,data):
        if data < self.data: # go left
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)

        else:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)

    def search(self,target):
        if self.data == target:
            print("Found")
        elif target < self.data:
            if self.left is None:
                print("Not found")
            else:
                self.left.search(target)
        else:
            if self.right is None:
                print("Not Found")
            else:
                self.right.search(target)

    def lookup(self,target,parent=None):
        if self.data == target:
            return self,parent
        elif target < self.data:
            if self.left is None:
                return None,None
            else:
                return self.left.lookup(target,self)
        else:
            if self.right is None:
                return None, None
            else:
                return self.right.lookup(target,self)
        
    def delete(self,target):
        node, parent = self.lookup(target)
        if node != None and parent != None:
            # 0 child
            if node.left == node.right == None:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
            elif (node.left is None) != (node.right is None):
                # link parent to node child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n

            else: # 2 children
                curr = node # succ's parent
                succ = node.right
                while succ.left:
                    # ends when succ points at smallest child in right sub tree
                    curr = succ
                    succ = succ.left
                 # replace node's data with succ's data
                node.data = succ.data
                if curr.left is succ:
                    curr.left = succ.right
                else:
                    curr.right = succ.right # e.g. when curr is the parent
                
    def inorderIter(self): # iterative version
        s = [self] # initialise stack
        curr = self
        while s != []:
            if curr.left: # keep going left
                
                curr = curr.left
                s.append(curr)

            else: # curr.left is None
                curr = s.pop() # pop from stack
                print(curr.data)
                if curr.right: # check right
                    s.append(curr.right)
                    curr = curr.right
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()
            
                                
b = BST(10)
b.insert(5)
b.insert(15)
b.insert(2)
b.insert(7)

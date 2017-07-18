class BST:

    def __init__(self,size):
        self.left = [None for _ in range(size)]
        self.right = [None for _ in range(size)]
        self.root = [None for _ in range(size)]
        self.nextFree = 0

    def insert(self,data,index=0): # recursive insert
        print(index)
        if self.root[0] is None: # check if root is empty 
            self.root[0] = data
            self.nextFree += 1
        else:
            currData = self.root[index]
            print(currData)
            if data < currData: # go left subtree
                if self.left[index] == None:
                    self.left[index] = self.nextFree
                    print("self.left[index] = self.nextFree")
                    self.root[self.nextFree] = data
                    self.nextFree += 1
                else:
                     self.insert(data, index = self.left[index])

            else: # go right subtree
                if self.right[index] == None:
                    self.right[index] = self.nextFree
                    print("self.right[index] = self.nextFree")
                    self.root[self.nextFree] = data
                    self.nextFree += 1
                else:
                    self.insert(data,self.right[index])

    def search(self,target,index=0):
        if index is None:
            return "{} is not found".format(target)
        else:
            currData = self.root[index]
            if currData == target:
                return "FOUND"
            elif target<currData: # go left
                return self.search(target,self.left[index])
            else: # go right
                return self.search(target, self.right[index])

    def lookup(self,target,index=0,parent = None):
        if index is None:
            print("{} is not found".format(target))
            return None, None
        else:
            currData = self.root[index]
            parentIndex = index
            if currData == target:
                return index, parent
            elif target<currData: # go left
                return self.lookup(target,self.left[index],parentIndex)
            else: # go right
                return self.lookup(target, self.right[index],parentIndex)

    def inorder(self, index=0):
        if index is not None: # if it's None means there is nothing to display
            currData = self.root[index]
        if self.left[index] is not None:
            self.inorder(index=self.left[index])
        print(currData)
        if self.right[index] is not None:
            self.inorder(index=self.right[index])

    def preorder(self, index=0):
        if index is not None: # if it's None means there is nothing to display
            currData = self.root[index]
        print(currData)
        if self.left[index] is not None:
            self.inorder(index=self.left[index])
        
        if self.right[index] is not None:
            self.inorder(index=self.right[index])

    def delete(self,target):
        # screw this shit.
b = BST(10)
b.insert(10)
b.insert(5)
b.insert(20)
b.insert(1)
b.insert(25)

    
            
        
                    
                 

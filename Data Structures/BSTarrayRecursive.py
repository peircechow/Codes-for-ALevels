


class BST:

    def __init__(self,size):
        self.left = [None for _ in range(size)]
        self.right = [None for _ in range(size)]
        self.root = [None for _ in range(size)]
        self.freePositions = [i for i in range(size)]

    def getNextFree(self): # actually on second thoughts i think i can combine this with setPositions
        #if i do sth like freeIndex = self.freePositions[0] and then i setpositions() it will return the new one instead of the old one
        return self.freePositions[0]

    def setPositions(self):
        # after u getNextFree
        # removes first element
        print(str(self.freePositions[0]) + " is removed")
        self.freePositions = self.freePositions[1:]

    def addFree(self,index):
        self.freePositions = [index] + self.freePositions

    def isFull(self):
        # means no more space to insert
        return len(self.freePositions == 0)

    
# in the following functions, index is the pointer to the current
# element (or "Node") we are looking. index = self.left[index] to go to
# the left element recursively and vice-versa    
    def insert(self,data,index=0): # recursive insert
        print(index)
        if self.root[0] is None: # check if root is empty 
            self.root[0] = data
            self.setPositions()
        else:
            currData = self.root[index]
            print(currData)
            if data < currData: # go left subtree
                if self.left[index] is None:
                    self.left[index] = self.getNextFree()
                    print("self.left[index] = self.nextFree")
                    self.root[self.getNextFree()] = data
                    self.setPositions()
                else:
                     self.insert(data, index = self.left[index])

            else: # go right subtree
                if self.right[index] is None:
                    self.right[index] = self.getNextFree()
                    print("self.right[index] = self.nextFree")
                    self.root[self.getNextFree()] = data
                    self.setPositions()
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
        # in this case index means targetIndex (index of the ele that u want to del)
        index, parentIndex = self.lookup(target) # returns curr and its parent
        if self.left[index] == self.right[index] == None:
        # 0 children
           #check left
            if self.left[parentIndex] == index: # check if parent's left child is the target
                self.left[parentIndex] = None # points to nothing
                # self.root[index] = None # delete the root
            else: # not left means right
                self.right[parentIndex] = None
                # self.root[index] = None
            self.addFree(index)
                
        elif (self.left[index] is None) != (self.right[index] is None):# rmb parantheses please
            print('1 child')
        # 1 child: link parent to child
            if self.left[index]:
                childIndex = self.left[index]
            else:
                childIndex = self.right[index]
            # check if parent's left or parent's right
            if self.left[parentIndex] == index:
                #link parent to child
                self.left[parentIndex] = childIndex
            else:
                self.right[parentIndex] = childIndex
            # self.root[index] = None
            # self.left[index] = self.right[index] = None # change targetIndex to null pointer
            self.addFree(index)
        else:
            # 2 children oh shit.
            #reach into smallest in right sub tree
            curr ,succ = index, self.right[index]
            while self.left[succ]:
                # succ reaches into the smallest val in right sub tree
                curr = succ
                succ = self.left[curr]

            # link parent to succ, and curr to self.right[succ]
            self.right[parentIndex] = succ
            self.left[curr] = self.right[succ]
            self.addFree(index)

            


b = BST(10)
a = [10,5,20,1,7,30]
for e in a:
    b.insert(e)


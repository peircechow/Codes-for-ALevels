class BST:
    def __init__(self):
        self.tree = [None for _ in range(1000)]
        # 1D array BST

    def left_index(self,i):
        return 2*i+1

    def right_index(self,i):
        return 2*i+2

    def insert(self,data):
        root = 0
        if self.tree[root] is None:
            self.tree[root] = data
        else:
            curr = root
            while self.tree[curr] is not None:
                left = self.left_index(curr)
                right = self.right_index(curr)
                if data < self.tree[curr]:
                    # go left
                    if self.tree[left] is None:
                        self.tree[left] = data
                        return True
                    else:
                        curr = left
                else: # go right
                    if self.tree[right] is None:
                        self.tree[right] = data
                        return True
                    else:
                        curr = right
    def search(self,data):
        prev, curr = None, 0
        while curr is not None:
            if self.tree[curr] == data:
                return curr
            elif data < self.tree[curr]:
                # go left
                curr = self.left_index(curr)
            else:
                curr = self.right_index(curr)
        return False

    def lookup(self,data):
        prev, curr = None, 0
        while curr is not None:
            if self.tree[curr] == data:
                return curr,prev
            elif data < self.tree[curr]:
                # go left
                prev = curr
                curr = self.left_index(curr)
            else:
                prev = curr
                curr = self.right_index(curr)
        return None, None

    def shiftUp(self,prev,curr):
        # shift curr node to prev position for BST delete
        self.tree[prev] = self.tree[curr]
        self.tree[curr] = None # set to None as you have alreay moved it up
        # need to shift the two branches to prev's children
        if self.tree[self.left_index(curr)] is not None: # check left
            prevLeft = self.left_index(prev)
            self.shiftUp(prevLeft,self.left_index(curr))
        if self.tree[self.right_index(curr)] is not None: # check right
            prevRight = self.right_index(prev)
            self.shiftUp(prevRight,self.right_index(curr))
            
    def delete(self,data):
        curr,parent = self.lookup(data)
        if self.tree[self.left_index(curr)] is None and self.tree[self.right_index(curr)] is None:
            # 0 Child so just set curr to None
            self.tree[curr] = None # checked
            print("0 Child")
        elif (self.tree[self.left_index(curr)] is None) != (self.tree[self.right_index(curr)] is None):
            # 1 child
            # check left and right, and shift the respective one up
            if self.tree[self.left_index(curr)] is not None:
                # shift left child up to replace curr data
                self.shiftUp(curr,self.left_index(curr))
            else:
                self.shiftUp(curr,self.right_index(curr))
            print("1 child")

        else:
            # 2 child
            succParent, succ = curr, self.right_index(curr)
            print("2 child")
            while self.tree[self.left_index(succ)] is not None:
                succParent = succ
                succ = self.left_index(succ)
            # now succ is the smallest value in the right sub tree
            # replace curr data with succ data
            self.tree[curr] = self.tree[succ]
            # remove succ
            self.tree[succ] = None
            # check for succ to shift its children data up
            if self.tree[self.right_index(succ)] is not None:
                self.shiftUp(succ,self.right_index(succ))


    def inorder(self,i=0):
        if self.tree[self.left_index(i)] is not None:
            self.inorder(self.left_index(i))
        print(self.tree[i], end = ' ')
        if self.tree[self.right_index(i)] is not None:
            self.inorder(self.right_index(i))
    
                


b = BST()
b.insert(90)
b.insert(80)
b.insert(100)
b.insert(95)
b.insert(1005)
b.insert(500)
b.insert(1500)


        
    

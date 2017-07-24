def binarySort1(A): # one liner implementation
    # accepts a sorted array and sort in the order to be inserted into the BST
    # recursively similar to quicksort
    # root + left + right
    return [A[len(A)//2]] + binarySort1(A[:len(A)//2]) + binarySort1(A[len(A)//2+1 :]) if A != [] else []
    
def binarySort2(A): # normal implementation
    if A == []:
        return []
    else:
        return [A[len(A)//2]] + binarySort2(A[:len(A)//2]) +  binarySort2(A[len(A)//2+1 :])


def quicksortIterative(A):

    def partition(A): # takes in an unsorted array and return less equal more
        less = []
        equal = []
        more = []
        pivot = A[0]
        for item in A:
            if item<pivot:
                less.append(item)
            elif item==pivot:
                equal.append(item)
            else:
                more.append(item)
        return less,equal,more

    s = Stack()
    A = [6,2,6,3,4,6,9,5,3,2,34]
    less, equal, more = partition(A)
    s.push(more)
    s.push(equal)
    s.push(less)
    out = []

    while not s.isEmpty(): #your keep doing until your stack is empty
        if len(s.peek()) <= 1:
            for i in s.peek():
                out.append(i)
            s.pop() # remove that element

        else: # need to sort this array
            unsorted = s.pop()
            lessEqualMore = partition(unsorted)
            moreEqualLess = lessEqualMore[::-1]
            for i in range(len(moreEqualLess)): # more equal less
                array = moreEqualLess[i]
                if array != []:
                    #if isEqual(array):
                    if i == 1: # array of pivot ie all equal
                        for item in array:
                            s.push([item])
                    else:
                        s.push(array)

    print(out)


        
    

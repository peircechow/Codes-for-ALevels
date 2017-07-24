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
    def part(A):
        less,equal,more = [],[],[]
        pivot = A[0]
        for item in A:
            if item<pivot:
                less.append(item)
            elif item == pivot:
                equal.append(item)
            else:
                more.append(item)
        return more,equal,less
    
    stack = [arr for arr in part(A)]
    sortedArray = []
    while stack != []:
        array = stack.pop()
        
        if len(array) == 1: # [3] or [4] that kind
            #print(array[0])
            sortedArray.append(array[0])  # remove so dont have to sort
        elif array == []:
            pass
        else:
            moreEqualLess = part(array)
            for i in range(len(moreEqualLess)):
                subArr = moreEqualLess[i]
                if i == 1:
                    for item in subArr:
                        stack.append([item])
                else:
                    stack.append(subArr)
    return sortedArray



        
    

def binarySort1(A): # one liner implementation
    # accepts a sorted array and sort in the order to be inserted
    #into BST

    # recursively similar to quicksort
    # root + left + right
    return [A[len(A)//2]] + binarySort1(A[:len(A)//2]) + binarySort1(A[len(A)//2+1 :]) if A != [] else []
    
def binarySort2(A): # normal implementation
    if A == []:
        return []
    else:
        return [A[len(A)//2]] + binarySort2(A[:len(A)//2]) +  binarySort2(A[len(A)//2+1 :])

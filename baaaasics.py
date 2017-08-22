
def padding(): #pad left or right
    binNumber = 10010
    print('{}'.format(str(binNumber)).rjust(8,'0'))
    # "00010010"

def validateDate():
    import datetime
    correctDate = None
    try:
        newDate = datetime.datetime(2008,11,42) #YYYY,MM,DD
        correctDate = True
    except ValueError:
        correctDate = False
    print(str(correctDate))

def diffDates(): # takes the difference of dates
    import datetime as d
    d1 = d.datetime(2017,1,20) # year month day
    d2 = d.datetime(2000,1,30) 
    print((d1-d2).days) # d.timedelta(days)

def XDaysAfter():
    import datetime as d
    d1 = d.datetime(2017,1,20)
    daysAfter = 90
    print("{} after {} is {}".format(daysAfter, d1, d1+d.timedelta(daysAfter))
          
def timeInterval():
    # https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings 
    from datetime import datetime
    s1 = '10:33:26' 
    s2 = '11:15:49' # for example
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)

          
#-------------------------------OTHER RANDOM ALGOS-----------------------------------------#


def checkDuplicate(A):
    # http://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/ 
    
    import random as r
    size = 10
    A = [r.randint(1,size-1) for _ in range(size)]
    print(A)
    # condition is that array is length of n
    # and numbers are in the range of 0 to n-1 # currently does not work for 0
    # we do this in O(n) time complexity and O(1) extra space

    for i in range(len(A)):
        index = abs(A[i]) # if the same index is used twice, it will visit the negative element the second time
        # check if negative or positive
        if A[index] > 0:
            # mark as negative (ie "visited")
            A[index] = -A[index]
        else: # encountered a duplicated index as it is negative
            print(index)
    
          
          
def subsetSum(A,n):
    if len(A) == 0 or n<=0:
        return False
    if A[0] == n: # matches
        return [A[0]] # list containing first element for list concatanation
    sumValue = subsetSum(A[1:],n-A[0])
    if sumValue:
        return [A[0]] + sumValue
    else:
        # move to next value or take the first value 
        return subsetSum(A[1:],n) or subsetSum(A[1:],n-A[0])

